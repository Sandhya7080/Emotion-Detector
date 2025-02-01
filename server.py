from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector  # Ensure the import is correct

# Initialize Flask app
app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    Detects the dominant emotion from the provided text.
    
    This function extracts the 'text' field from the incoming JSON request, passes it to 
    the emotion detection model, and returns the result in a JSON format. If the dominant
    emotion is not detected, it returns an error message.
    """
    data = request.json  # Extract JSON from request
    text = data.get("text", "")  # Get 'text' field safely

    # Assuming emotion_detector takes 'text' as an argument and returns a result
    result = emotion_detector(text)  # Call the imported function with text

    # Check if dominant emotion is None and return a custom error message
    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == "__main__":
    """
    Run the Flask app on host 0.0.0.0 and port 5500 for incoming requests.
    Enables debug mode for development.
    """
    app.run(host="0.0.0.0", port=5500, debug=True)
