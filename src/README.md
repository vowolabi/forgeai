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


# Image and Video Caption Generator

This script provides a class `ImageCaptionGenerator` that can generate captions for both images and videos using a pre-trained vision-language model.

## Overview

The `ImageCaptionGenerator` class uses a combination of Vision Transformer (ViT) and GPT-2 models to generate natural language captions for visual content. It can process both individual images and video files, extracting frames from videos at a specified rate.

## Dependencies

- logging
- cv2 (OpenCV)
- transformers
- torch

## Class: ImageCaptionGenerator

### Initialization


caption_generator = ImageCaptionGenerator(model_name="bipin/image-caption-generator", max_length=128, num_beams=4)

model_name: The pre-trained model to use (default: "bipin/image-caption-gene)

## Methods

- extract_frames_from_blob(video_blob, frame_rate=0.25)

Extracts frames from a video blob at the specified frame rate.
Returns a list of image arrays.


- generate_caption(blob_content, is_image=False)

Generates captions for either an image or a video.
For videos, it extracts frames and generates captions for each frame.
Returns a concatenated string of all generated captions.


# Audio to Text Transcription Service

This script provides a function to transcribe audio files to text using OpenAI's Whisper model.

## Overview

The `audio2text` function takes a base64-encoded audio file as input, transcribes it to text using OpenAI's Whisper model, and then uploads the transcription to Azure Blob Storage.

## Dependencies

- logging
- base64
- openai
- src.util_func (custom module)
- settings (custom module)

## Function: audio2text

### Parameters

- `request`: A string containing a base64-encoded audio file.

### Process

1. Decodes the base64 audio data and saves it as a temporary MP3 file.
2. Reads the temporary file.
3. Sends the audio data to OpenAI's Whisper model for transcription.
4. Uploads the transcribed text to Azure Blob Storage.

### Returns

- The transcribed text.
- A dictionary containing:
  - `response`: The ID of the uploaded blob in Azure Storage.
  - `response_type`: Always set to "text".

## Note

This script requires valid API keys and configurations for OpenAI and Azure Blob Storage. Make sure to set these up in your environment or settings file.

## Security Warning

The OpenAI API key is hardcoded in this script. It is strongly recommended to use environment variables or a secure key management system instead of hardcoding sensitive information.

## Usage

This function is designed to be called by other parts of your application. Ensure that you have the necessary permissions and configurations set up before using it.


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


# XLNet-based Text Summarizer

This script provides a command-line interface (CLI) for summarizing text using the XLNet transformer model.

## Overview

The `SummarizerCLI` class implements a text summarization tool using the XLNet model from the `summarizer` library. It can take input text and generate a concise summary.

## Dependencies

- summarizer

## Class: SummarizerCLI

### Initialization

```python
summarizer = SummarizerCLI(text=None)
```

## Methods

- summarize_text()

Generates a summary of the provided text.
Returns the generated summary.
Prints the summary to the console.


- run()

Executes the summarization process.
Returns the result of summarize_text().


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
