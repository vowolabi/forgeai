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