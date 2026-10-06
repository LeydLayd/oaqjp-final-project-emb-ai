# Proyecto final: Emotion Detection con Python y Flask

Este repositorio contiene el proyecto final del curso IBM: Developing AI Applications with Python and Flask.

## Descripción

La aplicación desarrolla un sistema de detección de emociones en texto utilizando Python, Flask y la API de IBM Watson NLP para analizar sentimientos y emociones en frases en inglés.

El proyecto incluye:
- Un backend desarrollado con Flask
- Una interfaz web simple para ingresar texto
- Llamadas a un servicio de reconocimiento emocional
- Visualización de las puntuaciones por emoción y la emoción dominante

## Objetivo del proyecto

Permitir analizar un texto y determinar la emoción predominante entre:
- anger
- disgust
- fear
- joy
- sadness

La aplicación devuelve la probabilidad asociada a cada emoción y señala la que domina en la frase analizada.

## Tecnologías utilizadas

- Python
- Flask
- HTML / Bootstrap
- Requests
- IBM Watson Emotion API

## Estructura del proyecto

```text
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── static/
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── README.md
├── LICENSE
└── .gitignore
```

## Cómo ejecutar la aplicación

1. Clona este repositorio:

```bash
git clone https://github.com/LeydLayd/oaqjp-final-project-emb-ai.git
cd oaqjp-final-project-emb-ai
```

2. Crea y activa un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Instala las dependencias:

```bash
pip install flask requests
```

4. Ejecuta la aplicación:

```bash
python server.py
```

5. Abre tu navegador en:

```text
http://localhost:5000/
```

## Endpoint principal

La API expone el siguiente endpoint:

```text
/emotionDetector?textToAnalyze=I am glad this happened
```

Este devuelve una respuesta con los valores de emociones y la emoción dominante.

## Ejemplo de salida

```text
For the given statement, the system response is
'anger': 0.0,
'disgust': 0.0,
'fear': 0.0,
'joy': 0.96 and
'sadness': 0.0.
The dominant emotion is joy
```

## Pruebas

El proyecto incluye pruebas unitarias para validar que el detector reconoce correctamente emociones comunes:

```bash
python -m unittest test_emotion_detection.py
```

## Nota

Este proyecto fue desarrollado como parte del curso de IBM sobre desarrollo de aplicaciones de inteligencia artificial con Python y Flask, aplicando conceptos de NLP y consumo de servicios externos para análisis de emociones.

## Autor

LeydLayd
