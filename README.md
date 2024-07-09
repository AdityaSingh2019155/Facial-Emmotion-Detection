# Real-Time Emotion Detection Using Webcam

This project implements real-time emotion detection using a webcam feed. It captures video frames, detects faces using Haar cascades, and analyzes the emotions of detected faces using the DeepFace library.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-Time Processing:** Emotion detection is performed on each frame captured from the webcam in real-time.
- **Face Detection:** Utilizes OpenCV's Haar cascade classifier to detect faces within each frame.
- **Emotion Recognition:** DeepFace library is employed to analyze facial expressions and determine dominant emotions such as happy, sad, angry, etc.
- **Visualization:** Draws rectangles around detected faces and overlays the predicted emotion as text.

## Demo
Include a brief GIF or video showcasing the real-time emotion detection in action.

## Installation
1. Clone the repository:

2. Navigate into the project directory:

3. Install dependencies:

Make sure you have Python 3.x installed on your system.

## Usage
- Run the script to start real-time emotion detection using your webcam:
- Press `q` to exit the application.

## Contributing
Contributions are welcome! Here's how you can contribute:
- Fork the repository
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes
- Commit your changes (`git commit -am 'Add new feature'`)
- Push to the branch (`git push origin feature-branch`)
- Create a new Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
