FROM python:3.7.9-slim-buster

LABEL manteiner="JJQuispe" \
    manteiner_mail="joelquispeunju@gmail.com"

ENV APP_HOME /usr/src
ENV PYTHONPATH $APP_HOME
WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY ./app $APP_HOME/app
COPY Procfile $APP_HOME

EXPOSE 8000

RUN ls

ENTRYPOINT [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
