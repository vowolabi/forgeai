import base64
import logging
import os


from src.imageCaptionGenerator import ImageCaptionGenerator
from src.summarize import SummarizerCLI
from settings import *
from src.util_func import upload_data_to_blob


def video_caption(blob):
    try:
        # Get the path of the newly added image
        logging.info(f"Python blob trigger function processed blob")

        temp_file_path = '/tmp/decoded_video.mp4'
        # Read the image content
        try:
            # Decode the base64 content
            blob_str = blob.split(sep=',')[1]
            # Add padding if necessary
            missing_padding = len(blob_str) % 4
            logging.info(missing_padding)
            if missing_padding:
                blob_str += '=' * (4 - missing_padding)
            decoded_bytes = base64.b64decode(blob_str)

            # Save the decoded bytes to a file in the /tmp directory

            with open(temp_file_path, 'wb') as video_file:
                video_file.write(decoded_bytes)

            logging.info(f"Video file saved successfully to {temp_file_path}.")

            # Load the file from the temporary location
            with open(temp_file_path, 'rb') as video_file:
                video_content = video_file.read()

            # Process the video content (example: logging the size of the file)
            logging.info(f"Loaded video file from {temp_file_path}, size: {len(video_content)} bytes.")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
                logging.info(f"Temporary file {temp_file_path} deleted.")

        # Check if the image content is not empty
        if video_content:
            logging.info(f"{type(video_content)}")
            logging.info("Image content read successfully.")

            # Your existing code to process the image and generate caption

            caption_generator = ImageCaptionGenerator()
            logging.info("Image caption generator initialised")

            caption = caption_generator.generate_caption(video_content)
            logging.info(caption)

            summarizer = SummarizerCLI(text=caption)
            logging.info("Summarizer initialised")

            summary = summarizer.run()

            logging.info(f"Generated caption: {summary}")
            id = upload_data_to_blob(CONTAINER_NAME, summary, 'txt')
            return summary, {"response": id, "response_type": "text"}


        else:
            logging.error("Failed to read image content. Image is empty.")

    except Exception as e:
        logging.error(f"Error processing blob: {e}")
