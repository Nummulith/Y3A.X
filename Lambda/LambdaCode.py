import json
import boto3
import logging

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    bucket_name = 'pavel-endpoint-bucket'

    key = 'text.txt'
    try:
        s3.put_object(Bucket=bucket_name, Key=key, Body=b'This is a test')
        logging.info(f'Successfully put object in {bucket_name}')
        res = "ok"
    except Exception as e:
        logging.error(f'Error putting object: {e}')
        res = "fail"

    key = 'map.png'
    try:
        response = s3.get_object(Bucket=bucket_name, Key=key)
        logging.info(f'Successfully got object from {bucket_name}: {response["Body"].read()}')
        res += ", ok"
    except Exception as e:
        logging.error(f'Error getting object: {e}')
        res += ", fail"

    return {
        'statusCode': 200,
        'body': f'Check completed: {res}'
    }
