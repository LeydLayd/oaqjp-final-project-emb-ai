import json
import requests


"""Funcion para evaluacion de emociones en texto"""


def emotion_detector(text_to_analyse):
  # Url a consultar
  url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
  # Cabezera con informacion
  header = {
      "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
  }
  # Texto a analizar
  myobj = {"raw_document": {"text": text_to_analyse}}

  # Consulta
  response = requests.post(url, json=myobj, headers=header)

  # Error de respuesta
  if response.status_code == 400:
    return {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

  # CORRECCIÓN: Convertir la respuesta HTTP a un diccionario de Python usando .json()
  formatted_response = response.json()

  # Extraemos el diccionario de emociones del primer elemento
  predicciones = formatted_response["emotionPredictions"][0]["emotion"]

  # 1. Extraer los puntajes individuales
  anger_score = predicciones["anger"]
  disgust_score = predicciones["disgust"]
  fear_score = predicciones["fear"]
  joy_score = predicciones["joy"]
  sadness_score = predicciones["sadness"]

  # 2. Encontrar la emoción dominante (la que tiene el valor máximo)
  dominant_emotion = max(predicciones, key=predicciones.get)

  # 3. Construir el nuevo diccionario con el formato deseado
  nuevo_formato = {
      "anger": anger_score,
      "disgust": disgust_score,
      "fear": fear_score,
      "joy": joy_score,
      "sadness": sadness_score,
      "dominant_emotion": dominant_emotion,
  }

  return nuevo_formato