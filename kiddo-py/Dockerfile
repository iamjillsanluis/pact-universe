FROM python:3.7.2-alpine
RUN apk update && apk upgrade && apk add --update gcc libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
