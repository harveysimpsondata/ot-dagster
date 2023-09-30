from duckdb import connect
from web3 import Web3
import polars as pl
import datetime
import requests
from concurrent.futures import ThreadPoolExecutor
from quickstart_etl.serviceAgreement import serviceAgreementABI

class Duck:

    def __init__(self):
        self.con = None

    def connectMD(self, motherDuck_token):
        self.con = connect(f'md:origintrail?motherduck_token={motherDuck_token}&saas_mode=true')
        return self

    def get_connection(self):
        if self.con is None:
            raise ValueError("No active connection!")
        else:
            return print(f"Connected! {self.con}")

    def createDuckTable(self):
        self.con.execute("""
            CREATE TABLE IF NOT EXISTS publishes 
            (MESSAGE VARCHAR(100), 
            ASSET_ID VARCHAR(100), 
            BLOCK_NUMBER INTEGER, 
            TIME_ASSET_CREATED TIMESTAMP, 
            TIME_OF_TRANSACTION TIMESTAMP, 
            TRAC_PRICE FLOAT, 
            EPOCHS_NUMBER INTEGER, 
            EPOCH_LENGTH_DAYS FLOAT, 
            PUBLISHER_ADDRESS VARCHAR(100), 
            SENT_ADDRESS VARCHAR(100), 
            TRANSACTION_HASH VARCHAR(100) PRIMARY KEY, 
            BLOCK_HASH VARCHAR(100))
        """)

    def getMaxBlock(self):
        result = self.con.execute("SELECT MAX(BLOCK_NUMBER) AS max_block FROM publishes").fetchone()
        if result[0] is not None:
            max_block_number = result[0]
            print(f"The maximum block number in the database is: {max_block_number}")
        else:
            max_block_number = 0
            print("Couldn't retrieve the maximum block number.")
        return max_block_number

    def load_to_motherduck(self, df):
        self.con.register('df', df)

        self.con.sql("""
            INSERT INTO publishes
            SELECT * FROM df
            ON CONFLICT (TRANSACTION_HASH)  -- this is the primary key
            DO NOTHING;
        """)

        df_length = df.height
        print(f"Inserted {df_length} rows into the Duck Nest!")


class EthRPC:

    def __init__(self, ONFINALITY_KEY):

        self.ONFINALITY_KEY = ONFINALITY_KEY
        self.w3 = Web3(Web3.HTTPProvider(f'https://origintrail.api.onfinality.io/rpc?apikey={ONFINALITY_KEY}'))
        self.contract_address = '0xB20F6F3B9176D4B284bA26b80833ff5bFe6db28F'
        self.abi = serviceAgreementABI

    def get_latest_block(self):
        latest_block = self.w3.eth.block_number - 1
        return latest_block

    def get_last_block50(self):
        get_last_block = self.w3.eth.block_number - 50
        return get_last_block

    def get_processed_events(self, from_block, latest_block):
        #latest_block = self.w3.eth.block_number - 1
        contract = self.w3.eth.contract(address=self.contract_address, abi=self.abi)
        events_list = contract.events.ServiceAgreementV1Created.get_logs(fromBlock=from_block, toBlock=latest_block)

        if len(events_list) > 0:
            processed_events = [{
                'assetContract': item['args'].get('assetContract', ''),
                'startTime': item['args'].get('startTime', ''),
                'epochsNumber': item['args'].get('epochsNumber', ''),
                'epochLength': item['args'].get('epochLength', ''),
                'tokenAmount': item['args'].get('tokenAmount', ''),
                'event': item.get('event', ''),
                'tokenId': item['args'].get('tokenId', ''),
                'transactionHash': item.get('transactionHash', '').hex() if item.get('transactionHash') else '',
                'blockHash': item.get('blockHash', '').hex() if item.get('blockHash') else '',
                'blockNumber': item.get('blockNumber', ''),
                'address': item.get('address', '')
            } for item in events_list]
        else:
            raise ValueError("No events found for the specified blocks.")

        return processed_events


class Transform:

    def __init__(self, processed_events, SUBSCAN_KEY, MAX_WORKERS):
        self.processed_events = processed_events
        self.SUBSCAN_KEY = SUBSCAN_KEY
        self.MAX_WORKERS = MAX_WORKERS

    def get_df(self):
        df_assets = (
            pl.DataFrame(self.processed_events)
            .with_columns([
                (pl.col("tokenAmount") / 1e18).alias("tokenAmount"),
                (pl.col("epochLength") / 86400).alias("epochLength"),
                pl.col("startTime").apply(lambda y: datetime.datetime.utcfromtimestamp(y).isoformat()).alias(
                    "startTime")
            ])
            .select([
                pl.col("assetContract").alias("ASSET_CONTRACT"),
                pl.col("startTime").alias("TIME_ASSET_CREATED"),
                pl.col("epochsNumber").alias("EPOCHS_NUMBER"),
                pl.col("epochLength").alias("EPOCH_LENGTH-(DAYS)"),
                pl.col("tokenAmount").alias("TRAC_PRICE"),
                pl.col("event").alias("EVENT"),
                pl.col("tokenId").alias("ASSET_ID"),
                pl.col("transactionHash").alias("TRANSACTION_HASH"),
                pl.col("blockHash").alias("BLOCK_HASH"),
                pl.col("blockNumber").alias("BLOCK_NUMBER"),
                pl.col("address").alias("EVENT_CONTRACT_ADDRESS")
            ]))

        # Get all transaction hashes
        hashes = df_assets['TRANSACTION_HASH'].to_list()

        def fetch_transaction_data(hash):
            subscan_url = "https://origintrail.api.subscan.io/api/scan/evm/transaction"
            headers = {
                "Content-Type": "application/json",
                "X-API-Key": self.SUBSCAN_KEY
            }
            data = {
                "hash": hash
            }
            response = requests.post(subscan_url, headers=headers, json=data).json()
            if response.get("code") == 0:
                data = response["data"]
                return {
                    "message": response["message"],
                    "generated_at": response["generated_at"],
                    "hash": data["hash"],
                    "from": data["from"],
                    "to": data["to"]["address"]
                }

        with ThreadPoolExecutor(max_workers=self.MAX_WORKERS) as executor:
            hash_list = list(executor.map(fetch_transaction_data, hashes))

        # Filter out any None values from the hash_list
        hash_list = [h for h in hash_list if h is not None]

        df_hash = (
            pl.DataFrame(hash_list)
            .with_columns(
                pl.col("generated_at")
                .apply(lambda y: datetime.datetime.utcfromtimestamp(y).isoformat()).alias("generated_at")
            )
            .select([
                pl.col("message").alias("MESSAGE"),
                pl.col("generated_at").alias("TIME_OF_TRANSACTION"),
                pl.col("hash").alias("TRANSACTION_HASH"),
                pl.col("from").alias("PUBLISHER_ADDRESS"),
                pl.col("to").alias("SENT_ADDRESS")
            ]))

        df = df_assets.join(df_hash, on="TRANSACTION_HASH", how="left")

        # Filter rows based on the MESSAGE column
        df = df.filter(pl.col("MESSAGE") == "Success")

        df = df.select(["MESSAGE",
                        "ASSET_ID",
                        "BLOCK_NUMBER",
                        "TIME_ASSET_CREATED",
                        "TIME_OF_TRANSACTION",
                        "TRAC_PRICE",
                        "EPOCHS_NUMBER",
                        "EPOCH_LENGTH-(DAYS)",
                        "PUBLISHER_ADDRESS",
                        "SENT_ADDRESS",
                        "TRANSACTION_HASH",
                        "BLOCK_HASH"])

        return df














