FROM postgres:13-buster
ENV LANG en_US.utf8

RUN apt update && apt upgrade -y
RUN apt install vim wget lsb-release bash-completion -y

RUN echo '\n\
source /usr/share/bash-completion/bash_completion\
' >> /root/.bashrc

WORKDIR /root/work
