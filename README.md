# SentinelCare: Advanced AI Fall Detection System

**Collaborators**: [Dr. Irshad Ibrahim](https://github.com/Dr-irshad) and [Umar Farooq](https://github.com/imumarfarooq)

## Overview

SentinelCare is an advanced AI-powered fall detection system utilizing pose estimation techniques to identify and alert for falls in real-time. This system is designed for use in healthcare facilities, elderly care homes, and smart surveillance applications to enhance safety and response times.

## Features

- **Real-Time Fall Detection**: Uses pose estimation models to identify abnormal postures indicative of falls.
- **High Accuracy**: Implements state-of-the-art deep learning models such as OpenPose, BlazePose, or MediaPipe Pose.
- **Edge & Cloud Deployment**: Works on edge devices like Raspberry Pi or cloud-based solutions for scalable applications.
- **Alerts & Notifications**: Sends alerts via email, SMS, or IoT-integrated platforms (e.g., AWS, Firebase, MQTT).
- **Customizable Sensitivity**: Adjustable thresholds for fall detection to reduce false positives.
- **Privacy-Preserving**: Uses skeletal representation instead of raw video footage to ensure privacy.

## Technologies Used

- **Programming Languages**: Python
- **Frameworks & Libraries**:
  - TensorFlow / PyTorch
  - OpenPose / MediaPipe / BlazePose
  - OpenCV
  - NumPy, Pandas
  - Flask / FastAPI (for API integration)
  - MQTT / Firebase / Twilio (for alerts)

## System Architecture

1. **Video Input**: Live camera feed or pre-recorded video.
2. **Pose Estimation Model**: Extracts skeletal keypoints from the video.
3. **Fall Detection Algorithm**:
   - Checks body orientation, velocity, and impact detection.
   - Uses machine learning classifiers (e.g., SVM, CNN, LSTM) for improved accuracy.
4. **Alert System**: Notifies caregivers through SMS, email, or IoT integration.
5. **Dashboard (Optional)**: Web-based UI for monitoring fall events in real-time.

## Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Virtual environment (optional but recommended)

### Setup

```sh
# Clone the repository
git clone https://github.com/Dr-irshad/SentinelCare-Advanced-AI-Fall-Detection-System.git
cd SentinelCare-Advanced-AI-Fall-Detection-System

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

Dataset
You can use publicly available fall detection datasets such as:

UR Fall Detection Dataset
Le2i Fall Detection Dataset
Fallen Person Dataset
Deployment
Edge Deployment (Raspberry Pi/Jetson Nano)

Optimize the model using TensorFlow Lite or ONNX
Use OpenVINO for Intel-based edge devices
Cloud Deployment

Deploy using AWS Lambda, Google Cloud Functions, or Azure Functions
Integrate with cloud storage and alert systems
Alerts & Notifications
Email Alerts: Configurable SMTP settings
SMS Alerts: Twilio API
IoT Integration: MQTT, Firebase, or WebSockets
Future Enhancements
Deep learning-based fall classification using LSTMs
Multi-camera support
Integration with wearable sensors
Contribution
We welcome contributions! Please open an issue or submit a pull request.
