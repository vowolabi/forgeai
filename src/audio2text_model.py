import logging
import base64

from openai import OpenAI
from src.util_func import upload_data_to_blob
from settings import *
def audio2text(request):
    logging.info(f'WRITING TO FILE')
    file_path = '/tmp/sample.mp3'  # Using /tmp for temporary storage
    with open(file_path, 'wb') as file:
        try:
            file.write(base64.b64decode(request.split(sep=',')[1]))
        except Exception as error:
            logging.info(f'{error}')
    logging.info(f'READING FILE')
    with open(file_path, 'rb') as file:
        content = file.read()
    logging.info(f'SENDING TO WHISPER')
    response = OpenAI(api_key=API).audio.transcriptions.create(
        model="whisper-1",
        file=("ew.mp3", content, "audio/mp3")
    ).text
    id = upload_data_to_blob(CONTAINER_NAME, response, 'txt')
    return response, {"response": id, "response_type": "text"}