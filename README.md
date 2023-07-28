# Gesture Control Project in Python


This is a gesture control project in Python that allows you to interact with your computer using hand gestures. The project supports 5 gestures: pause, play, volume up, volume down, and seek forward and backward. It utilizes computer vision techniques to recognize the gestures from a live video feed and the PyAutoGUI library to simulate keyboard inputs.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.10
- OpenCV library
- Mediapipe library
- PyAutoGUI library

You can install the required libraries using pip:

```bash
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

## Getting Started

Follow these steps to get the gesture control project up and running:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/mohaneesh-03/Gesture-Control.git
```

2. Navigate to the project directory:

```bash
cd gesture-control
```

3. Run the `gesture_control.py` script:

```bash
python gesture_control.py
```

## How to Use

Once the script is running, it will access your computer's camera to detect hand gestures. Here are the supported gestures and their corresponding actions:

### Pause and Play

To pause or play, show all five fingers open in front of the camera.

### Volume Up

Point your thumb up to increase the volume.

### Volume Down

Point your thumb down to decrease the volume.

### Seek Forward

Point your thumb right to seek forward.

### Seek Backward

Point your thumb left to seek backward.

Make sure the media player or application you want to control is in focus and active on your computer.

## Troubleshooting

If the gestures are not being recognized accurately, ensure the following:

1. Ensure proper lighting conditions for the camera feed.
2. Make sure your hand is clearly visible in the camera frame.
3. Try adjusting the volume of your system to check if volume gestures are working.

## Customization

This project provides a foundation for gesture control applications. You can extend it to support more gestures or integrate it into your own projects.

## Acknowledgments

This project is based on the work of the Mediapipe library, the OpenCV community, and the PyAutoGUI library.


---

Feel free to contribute to this project by submitting pull requests or creating issues for bug fixes or feature requests. Happy gesture controlling!
