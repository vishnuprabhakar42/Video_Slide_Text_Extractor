import cv2
import pytesseract
import os

# Directory containing the extracted frames
frames_dir = 'frames'
# Ensure Tesseract executable path is correct for your system
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Create output directory for extracted text files
if not os.path.exists('extracted_text'):
    os.makedirs('extracted_text')

# Loop through each frame image and extract text
for frame in os.listdir(frames_dir):
    if frame.endswith('.png'):
        img_path = os.path.join(frames_dir, frame)
        text = pytesseract.image_to_string(cv2.imread(img_path))
        output_path = os.path.join('extracted_text', f'{frame}.txt')
        with open(output_path, 'w') as f:
            f.write(text)

print("Text extraction complete.")
