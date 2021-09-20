FROM python:3.8

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["uvicorn", "predict-sentiment-api:app", "--host", "0.0.0.0", "--port", "8082"]