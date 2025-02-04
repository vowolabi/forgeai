# Video Caption Generator and Summarizer

This script provides a function to generate captions for videos using a pre-trained image captioning model and then summarize the captions. It processes base64-encoded video data, generates captions, summarizes them, and stores the result in Azure Blob Storage.

## Overview

The `video_caption` function takes a base64-encoded video as input. It decodes the video, processes it using an image captioning model to generate captions, summarizes the captions, and returns the summary along with metadata for storage.

## Dependencies

- base64
- logging
- os
- src.imageCaptionGenerator (custom module)
- src.summarize (custom module)
- settings (custom module)
- src.util_func (custom module)

## Function: video_caption

### Parameters

- `blob`: A string containing the base64-encoded video data.

### Process

1. Decodes the base64 video data.
2. Saves the decoded video to a temporary file.
3. Reads the video content from the temporary file.
4. Initializes the ImageCaptionGenerator.
5. Generates captions for the video frames.
6. Initializes the SummarizerCLI with the generated captions.
7. Summarizes the captions.
8. Uploads the summary to Azure Blob Storage.

### Returns

- The generated summary.
- A dictionary containing:
  - `response`: The ID of the uploaded blob in Azure Storage.
  - `response_type`: Always set to "text".

## Configuration

This script relies on configuration variables defined in a `settings.py` file, including:

- `CONTAINER_NAME`: The name of the Azure Blob Storage container where summaries are stored.

## Usage

This function is designed to be called by other parts of your application, typically in response to a new video being added to a system. It's not meant to be run directly from the command line.

## Error Handling

The script includes comprehensive error handling:
- Logs errors during the decoding and file operations.
- Cleans up temporary files even if an error occurs.
- Logs any exceptions that occur during the caption generation and summarization process.

## Temporary File Handling

The script creates a temporary file named `decoded_video.mp4` in the `/tmp` directory to process the video. This file is automatically deleted after processing, regardless of whether the operation succeeds or fails.

## Logging

The script uses Python's logging module extensively to track the progress and any issues that arise during execution. Make sure to configure logging appropriately in your main application.

## Note

- Ensure that the necessary permissions and configurations are set up for Azure Blob Storage.
- The ImageCaptionGenerator class should be properly implemented in the `src.imageCaptionGenerator` module.
- The SummarizerCLI class should be correctly implemented in the `src.summarize` module.
- The `upload_data_to_blob` function should be correctly implemented in the `src.util_func` module.

## Security Considerations

- The script handles base64-encoded data. Ensure that the input is properly sanitized and validated before processing.
- Temporary files are created in the `/tmp` directory. Ensure that this directory has appropriate access controls in your deployment environment.

## Performance Considerations

- Processing videos, especially long ones, can be computationally intensive. Consider implementing timeout mechanisms or processing limits for very large videos.
- The script currently loads the entire video into memory. For very large videos, you might need to implement streaming or chunked processing.