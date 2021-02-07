FROM python:3.7.9-slim-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app ./app

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
