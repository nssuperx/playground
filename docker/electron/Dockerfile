FROM ubuntu

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -y install sudo vim git

RUN apt-get update \
    && apt-get -y install xserver-xorg
    # && apt-get -y install xserver-xorg libgtkextra-dev libgconf2-dev libnss3 libasound2 libxtst-dev libxss1 libgtk-3-0

# RUN apt-get update \
#     && apt-get install -y language-pack-ja-base language-pack-ja fonts-noto-cjk fcitx-mozc \
#     && im-config -n fcitx

# windows用にビルドするために必要
# RUN dpkg --add-architecture i386 \
#     && apt-get update \
#     && apt-get install -y wine-stable wine32

# nodejsとyarnをインストールするために必要
RUN apt-get update \
  && apt-get install -y curl

# nodejsをインストール
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
    && apt-get install -y nodejs

# yarnをインストール
# RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
#     && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/+sources.list.d/yarn.list \
#     && apt-get update && apt-get install yarn

# ENV GTK_IM_MODULE=xim \
#     QT_IM_MODULE=fcitx \
#     XMODIFIERS=@im=fcitx \
#     DefalutIMModule=fcitx

# RUN locale-gen ja_JP.UTF-8  
# ENV LANG=ja_JP.UTF-8 \
#     LC_ALL=ja_JP.UTF-8

# add user
# ARG DOCKER_UID=1000
# ARG DOCKER_USER=docker
# ARG DOCKER_PASSWORD=docker

# RUN useradd -m ${DOCKER_USER}
# RUN gpasswd -a ${DOCKER_USER} sudo
# RUN echo ${DOCKER_USER}:${DOCKER_PASSWORD} | chpasswd

# USER ${DOCKER_USER}

# WORKDIR /home/${DOCKER_USER}/app
WORKDIR /home/root/app

