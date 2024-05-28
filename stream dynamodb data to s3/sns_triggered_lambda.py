import json
import base64
import boto3
import logging
import time  
import os

logger = logging.getLogger()

#set logger
logger.setLevel(logging.INFO)

TABLE_NAME = os.environ.get('DYNAMODB_TABLE_NAME')

def lambda_handler(event, context):
    # try:
    for record in event['Records']:
        try:
            message = record['Sns']['Message']
            logger.info(str(message))
            payload =json.loads(message)
            for item in payload:
                print("item", item)
                custom_object = transform_record(item)
                print("custom_object", custom_object)
                add_record_in_table(custom_object)                    

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return {
                'statusCode': 500,
                'body': json.dumps('Internal Server Error')
            }

#function to add data in database dynamodb table
def add_record_in_table(item_values):
    try:
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(TABLE_NAME)  # Replace 'your-table-name' with your DynamoDB table name
        table.put_item(Item=item_values)
        logger.info("Added record to DynamoDB table")
    except Exception as e:
        logger.error("Error adding record to DynamoDB table: %s", e)
        raise e

# function to transform incoming recored from sns
def transform_record(info_item):
    alert = {}
    body = info_item.get('body')
    device_info_list = info_item['body']['device_information']

# Iterating over device information
    for device_info in device_info_list:
        alert['device_id'] = device_info.get('device_id')
        alert['manufacturer'] = device_info.get('manufacturer')
        alert['model_number'] = device_info.get('model_number')
        alert['firmware_version'] = device_info.get('firmware_version')
        alert['device_type'] = device_info.get('device_type')
    event = body.get('event')
    alert['userId'] = info_item.get('userId')
    alert['timestamp'] = event.get('timestamp')

    return alert
