import json
import logging
import os

import azure.functions as func
from azure.data.tables import TableServiceClient
from azure.storage.blob import BlobServiceClient

from settings import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    connect_str = os.getenv("AzureWebJobsStorage")
    table_service = TableServiceClient.from_connection_string(conn_str=connect_str)
    table_client = table_service.get_table_client(TABLE_NAME)
    history = []
    try:
        for entity in table_client.list_entities():
            blob_service_client = BlobServiceClient.from_connection_string(connect_str)
            request_data = blob_service_client.get_blob_client(container=CONTAINER_NAME,
                                                               blob=entity['request']).download_blob().content_as_text()
            response_data = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=entity[
                'response']).download_blob().content_as_text()

            history.append({
                "type": entity['request_type'],
                "user": request_data,
                "type_response": entity['response_type'],
                "response": response_data,
            })

    except Exception as e:
        logging.error(f"Failed to retrieve data from table: {e}")
        return func.HttpResponse("Failed to retrieve data from table", status_code=500)

    # Return the result as JSON
    return func.HttpResponse(json.dumps(history, default=str), mimetype="application/json")
