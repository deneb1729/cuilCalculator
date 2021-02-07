FROM python:3.7.9-slim-buster

LABEL manteiner="JJQuispe" \
    manteiner_mail="joelquispeunju@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /usr/src

WORKDIR $APP_HOME

RUN pip install uvicorn[standard]

COPY app/ $APP_HOME/app
EXPOSE 8000 $PORT

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1
