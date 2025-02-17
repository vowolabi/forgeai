# To enable ssh & remote debugging on app service change the base image to the one below
# FROM mcr.microsoft.com/azure-functions/python:4-python3.7-appservice
FROM mcr.microsoft.com/azure-functions/python:4-python3.8-appservice

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /

RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libatlas-base-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /home/site/wwwroot
