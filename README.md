# Final Project: Emotion Detector Web Application

## Project Overview
This project is an AI-based web application developed using Python, Flask, and the Watson NLP Emotion Predict library. The application analyzes user-provided text to evaluate emotional tones (anger, disgust, fear, joy, sadness) and identifies the dominant emotion.

## Author & Course Details
- **Course:** Developing AI Applications with Python and Flask (Coursera / IBM)
- **Role:** Software Engineer

## Features
- **Emotion Analysis:** Integrates with Watson NLP API to process natural language text.
- **Python Packaging:** Encapsulated emotion detection functionality into a reusable Python package (`EmotionDetection`).
- **Web Interface:** Interactive frontend built with HTML, JavaScript, and deployed via Flask framework.
- **Error Handling:** Robust handling for blank inputs and HTTP 400 status codes.
- **Unit Testing:** Validated core functionality using Python `unittest`.
- **Code Quality:** Formatted and checked with `pylint` achieving a 10.00/10 rating.

## Repository Structure
EmotionDetection/
├── EmotionDetection/
│   ├── init.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── server.py
├── test_emotion_detection.py
└── README.md
## How to Run the Application

1. **Install Dependencies:**
   ```bash
   pip install requests flask pylint
   Run Unit Tests:

```bash
python test_emotion_detection.py
Execute Code Quality Check:
```
```Bash
pylint server.py
Launch Web Application:
```
```Bash
python server.py
```
Open your browser and navigate to http://localhost:5000 to access the interface.


---

### Hướng dẫn các bước cập nhật lên GitHub

1. **Mở file `README.md` trong VS Code:**
   * Dán đoạn mã Markdown trên vào file.
   * Nhấn phím **`Ctrl + S`** để lưu file.

2. **Cập nhật thay đổi lên GitHub:**
   Mở Terminal trong VS Code (`PS E:\coursera dwp301c>`) và chạy lần lượt 3 lệnh sau:

   ```powershell
   git add README.md
   git commit -m "Add project description to README.md"
   git push origin main
