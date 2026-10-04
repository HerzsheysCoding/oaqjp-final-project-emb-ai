"""Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze the text provided by the user and return the emotion analysis.
    Handles blank inputs or status code 400 errors by returning an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    dominant_emotion = response.get('dominant_emotion')

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given sentence, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
