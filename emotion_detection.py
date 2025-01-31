import requests
import json

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(URL, headers=Headers, json=input_json)

    if response.status_code == 200:
        response_dict = response.json()  # Convert response to dictionary
        
        # Extract emotion scores from response
        emotions = response_dict['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = emotions['sadness']
        
        # Find the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        
        return f"""
anger: {anger}
disgust: {disgust}
fear: {fear}
joy: {joy}
sadness: {sadness}
dominant_emotion: {dominant_emotion}
"""
    else:
        return {"error": f"Error: {response.status_code}, {response.text}"}  # Return error message in dictionary format
