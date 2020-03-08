FROM python:3.7.6-alpine

ADD requirements.txt /
RUN apk --update-cache \
    && pip install -r requirements.txt
    && mkdir /app
WORKDIR /app