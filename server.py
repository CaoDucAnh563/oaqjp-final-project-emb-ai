"""
Flask server module for the Emotion Detector web application.
Provides API endpoints to serve index UI and analyze text emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Route handler that takes text input from request arguments,
    invokes emotion_detector, and returns formatted string output.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Execute emotion analysis
    response = emotion_detector(text_to_analyze)

    # Task 7: Check if dominant_emotion is None (invalid/blank input)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given input, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    """
    Renders the primary application homepage (index.html).
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
