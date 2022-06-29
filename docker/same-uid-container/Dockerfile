FROM debian:latest

ARG USER_NAME
ARG USER_ID
ARG GROUP_NAME
ARG GROUP_ID

RUN useradd -s /bin/bash -m ${USER_NAME} && \
    usermod -u ${USER_ID} ${USER_NAME} && \
    groupmod -g ${GROUP_ID} ${GROUP_NAME} && \
    usermod -g ${GROUP_NAME} ${USER_NAME}

USER ${USER_NAME}
WORKDIR /mnt/work
CMD /bin/bash
