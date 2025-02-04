import logging
import os
import uuid
import json
import time
import azure.functions as func
from azure.data.tables import TableServiceClient
from azure.storage.blob import BlobServiceClient
from src.util_func import get_base64_information, upload_data_to_blob
from src.text2text_model import text2text
from src.audio2text_model import audio2text
from src.main_video_caption import video_caption
from src.main_image_caption import image_caption
from settings import *
import requests


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        # Get the input string from the request
        data = req.params.get('data')
        action = req.params.get('action')
        if not data or not action:
            req_body = req.get_json()
            data = data or req_body.get('data')
            action = action or req_body.get('action')

        if not data or not action:
            raise ValueError("Missing 'data' or 'action' parameter")

        # Connect to the Azure Blob Storage

        connect_str = os.getenv('AzureWebJobsStorage')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Create a container if it does not exist
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        if not container_client.exists():
            container_client.create_container()

        # Create a blob and upload the text
        file_type, extension, content = get_base64_information(data)
        logging.info(f'Content: {content}')
        blob_name = upload_data_to_blob(CONTAINER_NAME, content, extension)
        logging.info(f'Blob Name: {blob_name}')
        logging.info(f'Choosing Action: {action}')

        if action == "text2text":
            response, dic = text2text(content)
        elif action == "audio2text":
            response, dic = audio2text(content)
        elif action == "video2text":
            response, dic = video_caption(content)
        elif action == "image2text":
            response, dic = image_caption(content, extension)
        else:
            raise ValueError("Invalid action specified")

        # Connect to the Azure Table Storage
        table_service = TableServiceClient.from_connection_string(connect_str)
        table_client = table_service.get_table_client(TABLE_NAME)
        table_client.create_entity({
            'PartitionKey': str(time.time()) + str(uuid.uuid4()),
            'RowKey': str(time.time()) + str(uuid.uuid4()),
            'request': blob_name,
            'request_type': file_type,
            'response': dic['response'],
            'response_type': dic['response_type']
        })

        return func.HttpResponse(json.dumps({'response': response}), status_code=200)

    except ValueError as ve:
        logging.error(f'ValueError: {ve}')
        return func.HttpResponse(str(ve), status_code=400)
    except requests.RequestException as re:
        logging.error(f'RequestException: {re}')
        return func.HttpResponse("Error processing external request", status_code=500)
    except Exception as e:
        logging.error(f'Unexpected error: {e}', exc_info=True)
        return func.HttpResponse("An unexpected error occurred", status_code=500)



