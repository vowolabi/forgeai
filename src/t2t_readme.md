# Text-to-Text Generation Service

This script provides a function to generate text responses using a GPT-3.5-turbo model and store the results in Azure Blob Storage.

## Overview

The `text2text` function takes a text prompt as input, generates a response using the GPT-3.5-turbo model, and then uploads the response to Azure Blob Storage.

## Dependencies

- g4f.client
- src.util_func (custom module)
- settings (custom module)

## Function: text2text

### Parameters

- `request`: A string containing the input text prompt.

### Process

1. Initializes a client for the GPT model.
2. Sends the input text to the GPT-3.5-turbo model for completion.
3. Retrieves the generated response.
4. Uploads the response to Azure Blob Storage.

### Returns

- The generated text response.
- A dictionary containing:
  - `response`: The ID of the uploaded blob in Azure Storage.
  - `response_type`: Always set to "text".

## Configuration

This script relies on configuration variables defined in a `settings.py` file, including:

- `CONTAINER_NAME`: The name of the Azure Blob Storage container where responses are stored.

## Usage

To use this function in your application:

```python
from your_module import text2text

input_text = "Your prompt here"
response, metadata = text2text(input_text)

print("Generated response:", response)
print("Blob storage ID:", metadata["response"])