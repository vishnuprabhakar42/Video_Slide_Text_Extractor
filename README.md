# Video Slide Text Extractor

## Overview
The Video Slide Text Extractor is a tool designed to extract text from slides in a video. This project uses `ffmpeg` to convert a video into individual frames and `Tesseract` OCR to extract text from each frame.

## Features
- Extract frames from a video using `ffmpeg`.
- Extract text from each frame using `Tesseract` OCR.
- Save extracted text to individual files.

## Requirements
- `ffmpeg`
- `Tesseract` OCR
- `Python 3`
- Python libraries: `opencv-python`, `pytesseract`

## Installation

### Install ffmpeg
```bash
sudo apt update
sudo apt install ffmpeg
