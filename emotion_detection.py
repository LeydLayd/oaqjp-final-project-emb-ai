import requests
'''Funcion para evaluacion de emociones en texto'''
def emotion_detector(text_to_analyse):
    # Url a consultar
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Cabezera con informacion
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Texto a analizar
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Consulta
    response = requests.post(url, json = myobj, headers=header)
    return response.text
