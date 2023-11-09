from ot_publisher.duckpond import *
import os
from dotenv import load_dotenv
from dagster import asset, AssetExecutionContext
from typing import List

load_dotenv()
SUBSCAN_KEY = os.getenv("SUBSCAN_KEY")
MOTHERDUCK_KEY = os.getenv("MOTHERDUCK_TOKEN")
ONFINALITY_KEY = os.getenv("ONFINALITY_KEY")
MOTHERDUCK_TOKEN = os.getenv("MOTHERDUCK_TOKEN")
MAX_WORKERS = 1  # adjust this based on your system's capabilities


@asset(group_name="test", compute_kind="RPC API")
def extract(context) -> List[dict]:
    duck = Duck().connectMD(MOTHERDUCK_TOKEN)
    duck_connection = duck.get_connection()

    RPC = EthRPC(ONFINALITY_KEY)

    from_block = RPC.get_last_block500()
    latest_block = RPC.get_latest_block()-1
    duck_block = duck.getMaxBlock() - 1

    context.log.info(f"The latest block number is: {latest_block+1}")
    context.log.info(f"The last 50 blocks are: {from_block}")
    context.log.info(f"The last block in DuckDB is: {duck_block+1}")

    processed_events = RPC.get_processed_events(duck_block, latest_block)

    return processed_events


@asset(group_name="test", compute_kind="Polars & Subscan API")
def transformDF(context: AssetExecutionContext, extract: List[dict]) -> pl.DataFrame:
    df = Transform(extract, SUBSCAN_KEY, MAX_WORKERS).get_df()
    return df


@asset(group_name="test", compute_kind="MotherDuck API")
def load(context: AssetExecutionContext, transformDF: pl.DataFrame):
    duck = Duck().connectMD(MOTHERDUCK_TOKEN)
    duck_connection = duck.get_connection()
    context.log.info(f"MotherDuck connection: {duck_connection}")
    duck.load_to_motherduck(transformDF)


