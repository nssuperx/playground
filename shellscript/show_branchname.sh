#!/bin/sh
read -p 'add setting to .bashrc ok?(y/N):' yn
case $yn in
    [Yy]* )
        echo 'if [ -f /etc/bash_completion.d/git-prompt ]; then'
        echo '    export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[01;33m\]$(__git_ps1)\[\033[00m\]\$ ''
        echo 'fi'
        ;;
    * ) echo 'abort';;
esac
