FROM python:3.6-slim

RUN apt-get update && apt-get install -y \
    build-essential

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app