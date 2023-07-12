FROM node:latest

COPY ./package.json package.json
COPY ./vue.config.js vue.config.js
RUN npm install

COPY ./src /src
WORKDIR /src