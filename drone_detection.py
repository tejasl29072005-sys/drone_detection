from ultralytics import YOLO
import cv2

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")  # YOLO nano model

# Open webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Run YOLO detection
    results = model(frame)
    annotated_frame = results[0].plot()  # Annotate objects

    # Show webcam with detections
    cv2.imshow("Drone Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()