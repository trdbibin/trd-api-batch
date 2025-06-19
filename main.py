import os
import boto3
import requests
import json

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

def run():
    secret_name = os.environ['SECRET_NAME']
    config = get_secret(secret_name)

    print("Fetching data from Veeva Vault...")
    # TODO: Make API call, save CSV to S3, convert to Parquet, load to Snowflake
    print(f"Using client_id: {config['client_id']}")

if __name__ == "__main__":
    run()