FROM ubuntu:21.10

RUN apt update && apt upgrade -y
RUN apt install sudo vim -y

RUN useradd ns -m
RUN echo "ns:nspass" | chpasswd
RUN adduser ns sudo
USER ns
WORKDIR /home/ns
CMD /bin/bash
