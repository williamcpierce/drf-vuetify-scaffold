# pull official base image
FROM python:3.11-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install updates
RUN apt-get update && apt-get upgrade -y

# install packages
COPY ./server/requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# set source
COPY ./server/src /src
WORKDIR /src
