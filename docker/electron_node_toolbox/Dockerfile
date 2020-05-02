FROM node

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install libx11-xcb-dev libxtst6 libnss3 libgtk-3-0 libxss1 libasound2

WORKDIR /home/app

