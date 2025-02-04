# Azure Function: HTTP History Retrieval

This Azure Function provides an HTTP endpoint for retrieving the history of processed requests and responses stored in Azure Table Storage and Azure Blob Storage.

## Overview

The function fetches all entities from a specified Azure Table, retrieves the corresponding request and response data from Azure Blob Storage, and returns a JSON array containing the history of interactions.

## Configuration

### function.json

```json
{
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "route": "history",
      "methods": ["get", "post"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}

```

This configuration sets up an HTTP-triggered function with anonymous authentication, accessible via GET and POST methods at the /api/history route.


## Function: main
## Parameters

req: An HttpRequest object containing the request data (not used in this function).

## Process

Connects to Azure Table Storage using the connection string from environment variables.
Retrieves all entities from the specified table.
For each entity:

Connects to Azure Blob Storage.
Retrieves the request data from the blob specified by the entity's 'request' field.
Retrieves the response data from the blob specified by the entity's 'response' field.
Constructs a history entry with type, user request, response type, and response data.


Compiles all history entries into a list.
Returns the history list as a JSON response.

## Returns

An HttpResponse object containing the history data in JSON format.

Error Handling

Returns a 500 status code with an error message if there's a failure in retrieving data from the table or blobs.

## Dependencies

azure.functions
azure.data.tables
azure.storage.blob

## Environment Variables

AzureWebJobsStorage: Connection string for Azure Storage account.

## Configuration Variables (from settings)

TABLE_NAME: Name of the Azure Table containing the history records.
CONTAINER_NAME: Name of the Azure Blob Storage container containing the request and response data.

## Usage
Send a GET or POST request to the function's URL:

curl https://your-function-url/api/history