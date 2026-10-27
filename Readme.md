# Hand Gesture Volume Control 🎚️

Control your computer's system volume using hand gestures with Python, OpenCV, MediaPipe, and PyAutoGUI.

## 📌 Project Overview

Hand Gesture Volume Control is a real-time computer vision application that allows users to control their computer's volume using their thumb and index finger.

Instead of pressing physical keyboard buttons, the application uses a webcam to detect hand landmarks, calculate the distance between the thumb tip and index finger tip, and trigger volume-up or volume-down keyboard commands.

The goal of this project is to explore how computer vision can make human-computer interaction more natural, interactive, and hands-free.

## 🎯 Why I Built This Project

I wanted to explore how Python and computer vision could be used to interact with a computer without relying entirely on a keyboard or mouse.

This project helped me understand how webcam input, hand landmark detection, coordinate calculations, and desktop automation can work together in a single real-time application.

Rather than training a custom machine learning model, I used MediaPipe's pretrained hand landmark solution to detect key points on the hand and built my own gesture-based control logic around those points.

## ⚙️ Technologies Used

| Technology | Why I Used It |
|---|---|
| Python | Core programming language used to connect all components and implement the application logic. |
| OpenCV (`cv2`) | Captures webcam frames, flips the image, converts color spaces, draws visual markers, and displays the live video feed. |
| MediaPipe | Detects hand landmarks and provides the coordinates of key points on the hand. |
| PyAutoGUI | Sends keyboard commands to control the computer's volume. |

## 🧠 How It Works

The application follows a simple real-time processing pipeline:

1. **Webcam initialization:** OpenCV opens the default webcam and captures video frames continuously.
2. **Frame preprocessing:** Each frame is flipped horizontally to provide a mirror-like experience and converted from BGR to RGB for MediaPipe processing.
3. **Hand landmark detection:** MediaPipe identifies hand landmarks. The application uses landmark `4` for the thumb tip and landmark `8` for the index finger tip.
4. **Coordinate extraction:** Normalized landmark coordinates are converted into pixel coordinates using the frame's width and height.
5. **Distance calculation:** The application measures the distance between the two fingertips.
6. **Gesture interpretation:** The distance is compared against a fixed threshold to decide which volume command to trigger.
7. **System interaction:** PyAutoGUI sends a volume-up or volume-down key command.
8. **Live visualization:** OpenCV displays the webcam feed with hand landmarks and a line connecting the fingertips.

## 🔍 Understanding the Core Logic

### 1. Capturing webcam input

```python
cam = cv2.VideoCapture(0)
```

OpenCV's `VideoCapture` accesses the default camera, usually the built-in webcam. The application reads frames from it inside a continuous loop.

### 2. Detecting hand landmarks

```python
my_hands = mp.solutions.hands.Hands()
```

MediaPipe's Hands solution detects hand landmarks without requiring me to train a custom model.

A detected hand contains 21 landmarks. Each landmark has normalized `x`, `y`, and `z` coordinates.

For this project, I only need two landmarks:

- `4`: Thumb tip
- `8`: Index finger tip

### 3. Converting coordinates

```python
x = int(landmark.x * frame_width)
y = int(landmark.y * frame_height)
```

MediaPipe returns normalized coordinates rather than direct pixel positions.

Multiplying the normalized coordinates by the frame dimensions converts them into pixel positions, allowing OpenCV to draw circles and lines at the correct locations.

### 4. Measuring fingertip distance

The Euclidean distance between the thumb tip and index finger tip determines the gesture.

Conceptually:

```python
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
```

A larger distance means the fingertips are farther apart; a smaller distance means they are closer together.

The original implementation uses a threshold of `50` to distinguish between these two states.

### 5. Triggering volume commands

```python
if distance > 50:
    pyautogui.press('volumeup')
else:
    pyautogui.press('volumedown')
```

PyAutoGUI sends keyboard commands to the operating system. The operating system then handles the volume adjustment.

This is desktop automation, not direct access to the system's internal audio controls.

*Note: This example illustrates the intended logic. The current script should be corrected to calculate the actual distance and avoid sending commands on every frame before being treated as the final implementation.*

## 🚀 Features

- Real-time webcam processing
- Hand landmark detection
- Thumb and index fingertip tracking
- Distance-based gesture interpretation
- Visual fingertip markers and connecting line
- Keyboard-based system volume control
- Live video preview
- Keyboard shortcut to exit the application

## 🛠️ Installation

### Prerequisites

- Python installed on your computer
- A working webcam
- A compatible Windows environment
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Hand-Gesture-Volume-Control
```

Replace the placeholder URL with the actual repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

Create a `requirements.txt` file containing compatible versions of the libraries used in the project.

```bash
python -m pip install opencv-contrib-python==4.11.0.86 mediapipe==0.10.21 pyautogui
```

These versions are a starting point for the legacy MediaPipe Hands API used in this code. Use a compatible Python version and test the environment before deployment.

### 4. Run the application

```bash
python main.py
```

Make sure `main.py` matches the filename of your Python script.

## 🎮 How to Use

1. Run the Python application.
2. Allow access to your webcam if prompted.
3. Position your hand within the camera's view.
4. Keep your thumb and index finger visible.
5. Move the fingertips closer together or farther apart to trigger the current gesture logic.
6. Press `Esc` to close the application.

The exact gesture behavior depends on the configured threshold and the distance calculation used in the implementation.

## ⚠️ Current Limitations

- The application relies on a working webcam and sufficient lighting.
- Hand detection may become unreliable when the hand is partially hidden or outside the camera frame.
- The gesture threshold is fixed and may need adjustment for different camera resolutions or hand positions.
- The current implementation can send repeated volume commands rapidly because it processes commands continuously.
- The application triggers volume-up and volume-down commands; it does not currently map fingertip distance to an exact volume percentage.
- The application needs to run locally because PyAutoGUI controls the computer on which the Python process is running.
- The current implementation needs additional error handling for failed webcam reads and missing hand landmarks.

## 🔮 Future Improvements

- Add a cooldown mechanism to prevent repeated volume commands.
- Introduce gesture smoothing to reduce accidental volume changes.
- Add a configurable threshold for different users and camera setups.
- Map fingertip distance to a more intuitive volume-control range.
- Improve webcam failure handling and resource cleanup.
- Add a graphical interface for configuration.
- Package the application as a Windows executable using PyInstaller.
- Record a demonstration video showing the application in action.

## 📚 What I Learned

Through this project, I explored:

- Accessing and processing live webcam frames with OpenCV
- Understanding image color spaces and frame transformations
- Working with MediaPipe's hand landmark detection
- Converting normalized coordinates into pixel coordinates
- Using geometric distance to interpret hand gestures
- Connecting computer vision output to desktop automation
- Building a real-time application that combines multiple Python libraries

## 👨‍💻 Project Status

**Prototype — functional improvements and deployment are planned.**

This project demonstrates how pretrained computer vision models can be combined with custom Python logic to build an interactive application.

The next development phase focuses on improving gesture reliability, preventing repeated keyboard events, and packaging the application for Windows.

---

**Built with Python, OpenCV, MediaPipe, and PyAutoGUI.**