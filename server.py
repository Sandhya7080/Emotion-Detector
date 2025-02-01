from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def demo():
    return "hellow"
    
@app.route("/emotionDetector", methods=["POST"])
def emotionDetector():
    data = request.json  # Extract JSON from request
    text = data.get("text", "")  # Get 'text' field safely
    result = emotion_detector(text)  
    return jsonify(result)  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
