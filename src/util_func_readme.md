# Azure Blob Storage Utility Functions

This script provides utility functions for working with base64-encoded data and uploading content to Azure Blob Storage.

## Overview

The script contains two main functions:
1. `get_base64_information`: Extracts file type and extension from a base64-encoded string.
2. `upload_data_to_blob`: Uploads content to Azure Blob Storage.

## Dependencies

- logging
- azure.storage.blob
- os
- uuid

## Functions

### get_base64_information

#### Parameters
- `data_base64`: A string containing base64-encoded data with header information.

#### Returns
- `file_type`: The type of the file (e.g., 'image', 'audio').
- `extension_type`: The specific format of the file (e.g., 'jpeg', 'mp3').
- `content`: The actual base64-encoded content without the header.

#### Description
This function parses a base64-encoded string that includes header information. It extracts and returns the file type, extension, and the content itself.

### upload_data_to_blob

#### Parameters
- `container_name`: The name of the Azure Blob Storage container.
- `content`: The data to be uploaded.
- `extension`: The file extension for the blob.

#### Returns
- `blob_name`: The name of the uploaded blob (a UUID with the specified extension).

#### Description
This function uploads the given content to Azure Blob Storage. It generates a unique blob name using UUID, connects to Azure using the connection string from environment variables, and performs the upload.

## Configuration

The script requires the following environment variable:
- `AzureWebJobsStorage`: The connection string for Azure Blob Storage.

## Usage

Example usage of the functions:

```python
# Example for get_base64_information
base64_data = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/2wBDAA..."
file_type, extension, content = get_base64_information(base64_data)
print(f"File Type: {file_type}, Extension: {extension}")

# Example for upload_data_to_blob
container_name = "my-container"
content = b"Sample content to upload"
extension = "txt"
blob_name = upload_data_to_blob(container_name, content, extension)
print(f"Uploaded blob: {blob_name}")