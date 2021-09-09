FROM python:3.8-slim-buster
LABEL maintainer "Valentin.Fischer@gessmann.com"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./MQTT_to_WebHook.py MQTT_to_WebHook.py

