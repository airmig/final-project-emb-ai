"""
emotion_detector library
"""
import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    """
    emotion predict service
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    json_response = json.loads(response.text)
    anger = json_response['emotionPredictions'][0]['emotion']['anger']
    disgust = json_response['emotionPredictions'][0]['emotion']['disgust']
    fear = json_response['emotionPredictions'][0]['emotion']['fear']
    joy = json_response['emotionPredictions'][0]['emotion']['joy']
    sadness = json_response['emotionPredictions'][0]['emotion']['sadness']
    emotions = ['anger','disgust', 'fear', 'joy', 'sadness']
    emotion_values = [anger, disgust, fear, joy, sadness]
    max_value = max(emotion_values)
    max_index = emotion_values.index(max_value)
    dominant = emotions[max_index]
    response_emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant
    }
    return response_emotions