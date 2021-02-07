FROM python:3.7.9-slim-buster

LABEL manteiner="JJQuispe" \
    manteiner_mail="joelquispeunju@gmail.com"

ENV APP_HOME /usr/src
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME

RUN pip install -r requirements.txt

COPY ./app $APP_HOME/app
COPY Procfile $APP_HOME
COPY runtime.txt $APP_HOME

ENTRYPOINT uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
