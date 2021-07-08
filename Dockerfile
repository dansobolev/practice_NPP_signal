FROM python:3.8
ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /app/
