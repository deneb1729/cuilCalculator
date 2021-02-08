FROM python:3.7.9-slim-buster

LABEL manteiner="JJQuispe" \
    manteiner_mail="joelquispeunju@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /usr/src

WORKDIR $APP_HOME

RUN pip install fastapi uvicorn[standard]

COPY app $APP_HOME
EXPOSE 8000 $PORT

CMD uvicorn main:app --host "0.0.0.0" --port $PORT --workers 1 --log-level "debug"
