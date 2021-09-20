import logging
import warnings
import os

from werkzeug.exceptions import HTTPException
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.responses import JSONResponse
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import json

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
    
class Translator_en2pt:
    def __init__(self,
                 mname="Helsinki-NLP/opus-mt-en-roa"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(mname)
        self.tokenizer = AutoTokenizer.from_pretrained(mname)

    def __call__(self,
                 text):

        as_tensor = self.tokenizer.prepare_seq2seq_batch(src_texts=[text], return_tensors='pt')
        gen = self.model.generate(**as_tensor)
        translated = self.tokenizer.batch_decode(gen, skip_special_tokens=True)[0]


        return translated
    
class Translator_pt2en:
    def __init__(self,
                 mname="Helsinki-NLP/opus-mt-roa-en"):
        self.model = AutoModelForSeq2SeqLM.from_pretrained(mname)
        self.tokenizer = AutoTokenizer.from_pretrained(mname)

    def __call__(self,
                 text):

        as_tensor = self.tokenizer.prepare_seq2seq_batch(src_texts=[text], return_tensors='pt')
        gen = self.model.generate(**as_tensor)
        translated = self.tokenizer.batch_decode(gen, skip_special_tokens=True)[0]


        return translated

@app.on_event("startup")
async def load_model():
    global translator_en2pt, translator_pt2en
    translator_en2pt = Translator_en2pt()
    translator_pt2en = Translator_pt2en()
    logger.info('Loaded models!')

async def validate_json(request: Request):
    # makes the requests keys to keep the same order as the model

    try:
        body = await request.json()
    except:
        raise HTTPException(status_code=400, detail="Bad request")

    keys = ["text", "transformation"]
    for key in keys:
        if body.get(key) is None:
            raise HTTPException(status_code=400, detail="Bad request")

    return body

@app.post("/predict")
async def predict(token: dict = Depends(authenticate), data: dict = Depends(validate_json)):
    global translator_en2pt, translator_pt2en
    
    if data['transformation'] == 'en2pt':
        translation = translator_en2pt(data['text'])
    elif data['transformation'] == 'pt2en':
        translation = translator_pt2en(data['text'])
    else:
        translation = '<no translation available>'
    print(translation)
    return JSONResponse(
        status_code=200,
        content={'original_text': data['text'],
                 'translated_text':translation,
                 'transformation': data['transformation']})

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
