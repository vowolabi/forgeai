import logging

from azure.storage.blob import BlobServiceClient
import os, uuid


def get_base64_information(data_base64: str):
    logging.info("splitiing headerrrrrrrrrrrrrrrrrrrr")
    logging.info(data_base64[:100])
    header, content = data_base64.split(';', 1)
    file_type, extension_type = header.split(':', 1)[1].split('/')
    return file_type, extension_type, content


def upload_data_to_blob(container_name, content, extension):
    connect_str = os.getenv("AzureWebJobsStorage")
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_name = str(uuid.uuid4()) + "." + extension
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_client.upload_blob(content, overwrite=True)
    return blob_name
