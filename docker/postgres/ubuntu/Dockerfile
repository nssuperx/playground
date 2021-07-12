FROM ubuntu:21.04

RUN apt update && apt upgrade -y
RUN apt install vim wget lsb-release gnupg ca-certificates bash-completion -y
RUN apt install postgresql-client-13 -y

# install postgresql client
# RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \
#     wget --quiet -O - /tmp/pubkey.gpg https://www.postgresql.org/media/keys/ACCC4CF8.asc \
#     apt-key add /tmp/pubkey.gpg \
#     apt update \
#     apt install postgresql-client-13 -y

WORKDIR /home/work
CMD /bin/bash
