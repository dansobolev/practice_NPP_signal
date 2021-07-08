FROM python:3

WORKDIR /signal_project
COPY . /signal_project/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y ncat
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
