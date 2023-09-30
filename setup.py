from setuptools import find_packages, setup

setup(
    name="quickstart_etl",
    packages=find_packages(exclude=["quickstart_etl_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "RUST",
        "cargo",
        "duckdb==0.8.1",
        "dagster_duckdb",
        "dagster_duckdb_pandas",
        "boto3",
        "pandas",
        "polars",
        "web3",
        "requests",
        "python-dotenv",
        "matplotlib",
        "sqlescapy",
        "textblob",
        "tweepy",
        "wordcloud",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
