from setuptools import find_packages, setup

setup(
    name="ot_publisher",
    packages=find_packages(exclude=["ot_publisher_tests"]),
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
        "pyarrow",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
