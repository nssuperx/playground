FROM ubuntu:21.10

RUN apt update && apt upgrade -y
RUN apt install vim curl wget bash-completion -y

RUN { \
    echo ''; \
    echo 'source /usr/share/bash-completion/bash_completion'; \
} >> /root/.bashrc

WORKDIR /root
