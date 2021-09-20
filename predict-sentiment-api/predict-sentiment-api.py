import logging
import warnings
import os
import requests

from werkzeug.exceptions import HTTPException
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
import json
import oci
import jsonpickle
import pandas as pd
from datetime import datetime

import nltk
from nltk.stem import WordNetLemmatizer 

from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings("ignore", "Your application has authenticated using end user credentials")
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = FastAPI()

async def authenticate(request: Request):
    API_TOKEN = os.getenv('ACCESS_TOKEN') 
    token = request.headers.get("authorization")
    if (token is None) or (token != API_TOKEN):
        raise HTTPException(status_code=401, detail="Unauthorized")
    return {}

@app.on_event("startup")
async def load_model():
    global ai_client, lemmatizer
    
    nltk.download('wordnet')
    lemmatizer = WordNetLemmatizer()
    
    ai_client = oci.ai_language.AIServiceLanguageClient(oci.config.from_file(os.environ['OCI_CONFIG_URI']))

async def validate_json(request: Request):
    # makes the requests keys to keep the same order as the model

    try:
        body = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Bad request")
        
    keys = ["created_time", 'from', 'message', 'id', 'post_id']
    for key in keys:
        if json.loads(body).get(key) is None:
            raise HTTPException(status_code=400, detail="Bad request")

    return body

@app.post("/predict")
async def predict(token: dict = Depends(authenticate), data: dict = Depends(validate_json)):
    global ai_client, lemmatizer
    
    data = json.loads(data)
    url = os.environ['ADB_URL_CHECKIFEXIST']

    querystring = {"ID_":data['id']}

    headers = {"Content-Type": "application/json"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.json()['count_'] > 0:
        return JSONResponse(
            status_code=200,
            content={"row_already_on_db": "true"})

    url = f"http://{os.environ['TRANSLATIONAPI_LB_IP']}:8080/predict"
    
    payload = {
    "text": data['message'],
    "transformation": "pt2en"
    }
    headers = {
        "Content-Type": "application/json",
        "authorization": os.environ['AUTH_TOKEN_TRANSLATIONAPI']
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    translated_message = response.json()['translated_text']
    
    detect_language_sentiments_details = oci.ai_language.models.DetectLanguageSentimentsDetails(text=translated_message)
    output = ai_client.detect_language_sentiments(detect_language_sentiments_details)
    sentiment_analysis = output.data
    
    df = pd.DataFrame([{key: i.__dict__[key] for key in i.__dict__.keys() if key in ['_text', '_sentiment']} for i in sentiment_analysis.aspects])
    df['_text'] = df['_text'].apply(lambda x: [lemmatizer.lemmatize(i) for i in x.split()])
    
    updated_time = str(datetime.now())

    for i, row in df.iterrows():
        url = f"http://{os.environ['TRANSLATIONAPI_LB_IP']}:8080/predict"
    
        payload = {
        "text": ">>por<< " + row['_text'],
        "transformation": "en2pt"
        }
        headers = {
            "Content-Type": "application/json",
            "authorization": os.environ['AUTH_TOKEN_TRANSLATIONAPI']
        }

        response = requests.request("POST", url, json=payload, headers=headers)

        translated_back_message = response.json()['translated_text']

        url = os.environ['ADB_URL_INSERTCOMMENTS']

        payload = {"ID_": data['id'],
                          "POST_ID": data['post_id'],
                          "MESSAGE": data['message'][:32767],
                          "CREATED_TIME": data['created_time'],
                          "UPDATED_TIME": updated_time,
                          "TEXT_ELEMENT_EN": row['_text'],
                          "TEXT_ELEMENT_PT": translated_back_message,
                          "SENTIMENT": row['_sentiment']}
        
        headers = {"Content-Type": "application/json"}

        response = requests.request("POST", url, json=payload, headers=headers)

        print(response)
        print(response.text)
    
    return JSONResponse(
        status_code=200,
        content={"aspects": json.loads(jsonpickle.encode(sentiment_analysis))})

@app.get("/")
async def health_check():
    return JSONResponse(
        status_code=200,
        content={"message": "alive and running!"}
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": str(exc.detail)}
    )


@app.exception_handler(Exception)
async def handle_exception(*args):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal error"}
    )
