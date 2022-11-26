FROM node:16.15-alpine

COPY ./package.json package.json
RUN npm install

COPY ./src /src
WORKDIR /src