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