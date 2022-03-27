FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

# RUN apt-get update \
#     && apt-get -y install sudo vim git

RUN apt-get update \
    && apt-get -y install curl xserver-xorg libxcomposite-dev libnss3 libgtk-3-0 libasound2 openssh-server

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs
