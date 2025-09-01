from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Use a lightweight model for mobile

def detect_objects_from_camera():
    cap = cv2.VideoCapture(0)
    print("Opening camera...")
    ret, frame = cap.read()
    if not ret:
        cap.release()
        return "Failed to capture image."

    results = model(frame)
    labels = [model.names[int(box.cls)] for box in results[0].boxes]
    cap.release()
    return f"Detected objects: {', '.join(set(labels))}" if labels else "No objects detected."