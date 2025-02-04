# Image Caption Generator

This script provides a function to generate captions for images using a pre-trained image captioning model. It processes base64-encoded image data, generates a caption, and stores the result in Azure Blob Storage.

## Overview

The `image_caption` function takes a base64-encoded image and its file extension as input. It decodes the image, processes it using an image captioning model, and returns the generated caption along with metadata for storage.

## Dependencies

- base64
- logging
- os
- src.imageCaptionGenerator (custom module)
- settings (custom module)
- src.util_func (custom module)

## Function: image_caption

### Parameters

- `blob`: A string containing the base64-encoded image data.
- `e`: The file extension of the image (e.g., 'jpg', 'png').

### Process

1. Decodes the base64 image data.
2. Saves the decoded image to a temporary file.
3. Reads the image content from the temporary file.
4. Initializes the ImageCaptionGenerator.
5. Generates a caption for the image.
6. Uploads the caption to Azure Blob Storage.

### Returns

- The generated caption.
- A dictionary containing:
  - `response`: The ID of the uploaded blob in Azure Storage.
  - `response_type`: Always set to "text".

## Configuration

This script relies on configuration variables defined in a `settings.py` file, including:

- `CONTAINER_NAME`: The name of the Azure Blob Storage container where captions are stored.

## Usage

This function is designed to be called by other parts of your application, typically in response to a new image being added to a system. It's not meant to be run directly from the command line.

## Error Handling

The script includes comprehensive error handling:
- Logs errors during the decoding and file operations.
- Cleans up temporary files even if an error occurs.
- Logs any exceptions that occur during the caption generation process.

## Temporary File Handling

The script creates a temporary file in the `/tmp` directory to process the image. This file is automatically deleted after processing, regardless of whether the operation succeeds or fails.

## Logging

The script uses Python's logging module extensively to track the progress and any issues that arise during execution. Make sure to configure logging appropriately in your main application.

## Note

- Ensure that the necessary permissions and configurations are set up for Azure Blob Storage.
- The ImageCaptionGenerator class should be properly implemented in the `src.imageCaptionGenerator` module.
- The `upload_data_to_blob` function should be correctly implemented in the `src.util_func` module.

## Security Considerations

- The script handles base64-encoded data. Ensure that the input is properly sanitized and validated before processing.
- Temporary files are created in the `/tmp` directory. Ensure that this directory has appropriate access controls in your deployment environment.