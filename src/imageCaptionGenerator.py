import logging

import cv2
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch



class ImageCaptionGenerator:
    def __init__(self, model_name="bipin/image-caption-generator", max_length=128, num_beams=4):
        self.model = VisionEncoderDecoderModel.from_pretrained(model_name)
        self.feature_extractor = ViTFeatureExtractor.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.max_length = max_length
        self.num_beams = num_beams

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)

    @staticmethod
    def extract_frames_from_blob(video_blob, frame_rate=0.25):
        # Create a temporary file from the video blob
        video_stream = video_blob
        temp_file_path = 'temp_video.mp4'
        with open(temp_file_path, 'wb') as temp_file:
            temp_file.write(video_stream)
        # Open the video file with OpenCV
        cap = cv2.VideoCapture(temp_file_path)
        if not cap.isOpened():
            print("Error: Cannot open video stream or file")
            return []

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_interval = int(fps // frame_rate)

        image_arrays = []
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0:
                # Convert the frame from BGR to RGB
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image_arrays.append(frame_rgb)

            frame_count += 1

        cap.release()

        return image_arrays

    def generate_caption(self, blob_content, is_image=False):
        logging.info("Generating caption")
        if is_image:
            img_list = [blob_content]
        else:
            img_list = self.extract_frames_from_blob(blob_content)
        caption_list = []
        for img in img_list:
            #if img.mode != 'RGB':
                #img = img.convert(mode="RGB")

            pixel_values = self.feature_extractor(images=[img], return_tensors="pt").pixel_values.to(
                self.model.device)
            output_ids = self.model.generate(pixel_values, num_beams=self.num_beams, max_length=self.max_length)
            caption = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
            caption_list.append(caption)
        return ''.join(caption_list)


# Example usage:
if __name__ == "__main__":
    caption_generator = ImageCaptionGenerator()
    video_path = "test/data/miketyson.mp4"  # Replace with the actual path to your video
    with open(video_path, 'rb') as f:
        video_blob = f.read()

    frame_rate = 1  # Replace with the desired frame extraction rate (e.g., 1 frame per second)

    # Extract frames and get the list of image arrays
    generated_caption = caption_generator.generate_caption(video_blob)
    print("Generated Caption:", generated_caption)
