FROM python:3-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install debugpy

COPY requirements.txt .
RUN pip install -r requirements.txt || true
