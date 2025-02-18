import cv2
import numpy as np
from ultralytics import YOLO
import os

# Define the keypoint labels
keypoint_labels = [
    "Nose", "Left Eye", "Right Eye", "Left Ear", "Right Ear",
    "Left Shoulder", "Right Shoulder", "Left Elbow", "Right Elbow",
    "Left Wrist", "Right Wrist", "Left Hip", "Right Hip",
    "Left Knee", "Right Knee", "Left Ankle", "Right Ankle"
]

# Define keypoint pairs for drawing lines between connected keypoints
keypoint_connections = [
    (0, 1), (1, 3), (0, 2), (2, 4),
    (5, 6), (5, 7), (7, 9), (6, 8), (8, 10),
    (11, 12), (11, 13), (13, 15), (12, 14), (14, 16),
    (5, 11), (6, 12)
]

# Load the model
model = YOLO("yolo11n-pose.pt")  # Replace with your actual model path

# Function to check if a person is falling
def is_falling(keypoints):
    # Ensure we have at least 17 keypoints (for a complete detection)
    if len(keypoints) < 17:
        return False

    # Get key positions
    left_shoulder = np.array([keypoints[5][0], keypoints[5][1]])
    right_shoulder = np.array([keypoints[6][0], keypoints[6][1]])
    left_hip = np.array([keypoints[11][0], keypoints[11][1]])
    right_hip = np.array([keypoints[12][0], keypoints[12][1]])

    # Check if shoulders and hips are detected with sufficient confidence
    if (keypoints[5][2] < 0.3 or keypoints[6][2] < 0.3 or 
        keypoints[11][2] < 0.3 or keypoints[12][2] < 0.3):
        return False

    # Calculate the torso angle based on the shoulder and hip positions
    shoulder_midpoint = (left_shoulder + right_shoulder) / 2
    hip_midpoint = (left_hip + right_hip) / 2

    # Calculate the angle of the torso relative to the horizontal
    torso_vector = hip_midpoint - shoulder_midpoint
    torso_angle = np.arctan2(torso_vector[1], torso_vector[0]) * (180 / np.pi)

    # Calculate the vertical distance between shoulders and hips
    vertical_distance = abs(shoulder_midpoint[1] - hip_midpoint[1])

    # Debugging information
    print(f"Torso Angle: {torso_angle:.2f}, Vertical Distance: {vertical_distance:.2f}")

    # Fall detection criteria
    if (abs(torso_angle) < 20) and (vertical_distance < 40):
        return True  # Indicates a potential fall or lying down
    else:
        return False  # Indicates standing, walking, or seated

# Specify the input video file path
input_video_path = "/home/by4code/Desktop/patches-to=images/Fall-Detection/IMG_3926.MOV"  # Replace with your input video file path

# Start capturing from the input video file
cap = cv2.VideoCapture(input_video_path)

# Get video properties for output
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the output video writer
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "fall_detection_output-3926.mp4")
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("End of video or failed to capture frame")
        break

    # Predict keypoints on the current frame
    results = model(frame)

    for r in results:
        keypoints = r.keypoints.data.squeeze(0).numpy()

        if len(keypoints) < 17:
            continue  # Skip this frame if keypoints are incomplete

        # Check if the detected pose indicates a fall
        if is_falling(keypoints):
            cv2.putText(frame, "WARNING: Falling Detected!", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        else:
            cv2.putText(frame, "Rest Position", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        # Draw lines connecting the keypoints
        for connection in keypoint_connections:
            start_idx, end_idx = connection
            if start_idx >= len(keypoints) or end_idx >= len(keypoints):
                continue  # Skip if the keypoint indices are out of bounds

            x1, y1, conf1 = keypoints[start_idx]
            x2, y2, conf2 = keypoints[end_idx]

            if conf1 > 0.5 and conf2 > 0.5:
                cv2.line(frame, (int(x1), int(y1)), (int(x2), int(y2)), color=(255, 0, 0), thickness=2)

        # Draw labels for each keypoint
        for i in range(len(keypoints)):
            if keypoints[i][2] > 0.5:
                cv2.putText(frame, keypoint_labels[i],
                            (int(keypoints[i][0]), int(keypoints[i][1])),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Write the frame to the output video file
    out.write(frame)

# Release the capture, video writer, and close windows
cap.release()
out.release()

print("Pose estimation finished and video saved to:", output_path)
