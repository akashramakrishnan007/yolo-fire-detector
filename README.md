# Real-Time Fire Detection using YOLO

## Project Overview
This project implements a real-time fire detection system using a custom-trained YOLO object detection model.

The model was trained using Google Colab and deployed locally on Ubuntu for real-time webcam detection.

## Objective
The objective is to detect fire in real-time video and display:
- Bounding boxes
- Class labels
- Confidence scores

## Technologies Used
- Python
- YOLO / Ultralytics
- OpenCV
- PyTorch
- Google Colab
- Ubuntu

## Model
The trained YOLO model is provided as:

best.pt

Detected class:
- fire

## Real-Time Detection
The `detect.py` script loads the trained model and captures live video from the computer webcam.

Run the program using:

```bash
python detect.py