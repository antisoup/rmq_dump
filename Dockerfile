FROM python:3.10-alpine

WORKDIR /usr/src/app

RUN pip install pika

COPY . .

CMD python main.py
