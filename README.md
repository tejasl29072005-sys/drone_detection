YOLOv8 Real-Time Object Detection

This project implements a real-time object detection system using the **YOLOv8** (You Only Look Once) architecture and OpenCV. It captures video from a webcam, processes each frame through a pre-trained neural network, and displays the annotated results in a live window.


 Features
*   Real-time Processing:** Optimized for high-speed inference using the YOLOv8 Nano model.
*   Automatic Annotation:** Automatically draws bounding boxes and labels with confidence scores.
*   Simple Integration:** Uses the `ultralytics` library for seamless model management and `cv2` for video handling.

 Prerequisites
Before running the script, ensure you have Python installed along with the following libraries:

*   Ultralytics: For the YOLOv8 model and inference logic.
*   OpenCV:For video capturing and image rendering.
*   PyTorch: Required as the backend for Ultralytics.

Installation

1.  Clone the repository:**
    bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    

2.  Install dependencies:**
    bash
    pip install ultralytics opencv-python torch
    
Usage

1.  Run the main script:
    bash
    python main.py
    
2.  The webcam will open in a new window labeled **"Drone Detection"**.
3.  To exit the application, press the **'q'** key on your keyboard.

How It Works
Model Loading: The script initializes the `yolov8n.pt` weight file. If the file is not found locally, it will automatically download from the Ultralytics repository.
*   Frame Capture:`cv2.VideoCapture(0)` accesses the primary camera.
*   Inference: Each frame is passed to the model, which returns a list of detected objects.
*   Visualization:** The `.plot()` method generates a BGR image with boxes and labels overlaid on the original frame.

Project Structure
*   `main.py`: The primary Python script containing the detection loop.
*   `yolov8n.pt`: (Generated) The pre-trained Nano model weights.
*   `README.md`: Documentation for the project.

👨‍💻 Author
tejas L
Built as part of an AI/ML learning journey focused on real-time computer vision and deep learning systems.
