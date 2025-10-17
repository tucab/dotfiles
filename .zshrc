
# The following lines were added by compinstall

zstyle ':completion:*' completer _complete _ignored
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' matcher-list '' 'm:{[:lower:]}={[:upper:]}'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' original true
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle :compinstall filename '/home/juno/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall
# Lines configured by zsh-newuser-install
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=1000
unsetopt beep
bindkey -v
# End of lines configured by zsh-newuser-install

setopt HIST_IGNORE_DUPS
setopt HIST_SAVE_NO_DUPS
setopt SHARE_HISTORY

git_current_branch() {
    git rev-parse --abbrev-ref HEAD 2>/dev/null
}

alias ls="eza --icons=never --color=always"
alias n="nvim"
alias gg="exit"
alias rm="rm -i"
alias fastfetch2="fastfetch --config examples/16.jsonc"
alias ga="git add"
alias gcmsg="git commit --message"
alias ggpull='git pull origin "$(git_current_branch)"'
alias ggpush='git push origin "$(git_current_branch)"'
alias gc='git commit --verbose'
alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
eval "$(starship init zsh)"
export EDITOR="nvim"
export VISUAL="$EDITOR"
# export PATH="$PATH:/home/juno/.local/bin"
typeset -gU path
path=(
  /home/juno/.local/bin
  $path
)
brew () {
  unset -f brew
  eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
  brew "$@"
}
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
