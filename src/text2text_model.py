from g4f.client import Client
from src.util_func import upload_data_to_blob
from settings import *


def text2text(request):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": request}],
    ).choices[0].message.content
    id = upload_data_to_blob(CONTAINER_NAME, response, 'txt')
    return response, {"response": id, "response_type": "text"}
