#!/bin/bash
curl -s https://ohmyposh.dev/install.sh | bash -s
wget -P $HOME https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/1_shell.omp.json
if [ -f ~/.bashrc ]; then
    echo 'eval "$(oh-my-posh init bash --config ~/1_shell.omp.json)"' >> ~/.bashrc
else
    echo 'eval "$(oh-my-posh init bash --config ~/1_shell.omp.json)"' > ~/.bashrc
fi

