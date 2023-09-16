brew install jandedobbeleer/oh-my-posh/oh-my-posh
brew update && brew upgrade oh-my-posh
wget -P $HOME https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/1_shell.omp.json
if [ -f ~/.zshrc ]; then
    echo 'eval "$(oh-my-posh init zsh --config ~/1_shell.omp.json)"' >> ~/.zshrc
else
    echo 'eval "$(oh-my-posh init zsh --config ~/1_shell.omp.json)"' > ~/.zshrc
fi
exec zsh
