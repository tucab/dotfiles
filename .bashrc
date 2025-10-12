# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# Put your fun stuff here.

function git_current_branch() {
    git symbolic-ref --short HEAD 2>/dev/null || git rev-parse --short HEAD
}

alias ls="eza --icons=never --color=always"
alias n="nvim"
alias gg="exit"
alias fastfetch2="fastfetch --config example/16.jsonc"
alias ga="git add"
alias gcmsg="git commit --message"
alias ggpull='git pull origin "$(git_current_branch)"'
alias ggpush='git push origin "$(git_current_branch)"'
alias gc='git commit --verbose'
export EDITOR="nvim"
export VISUAL="$EDITOR"
export PATH="$PATH:/home/juno/.local/bin"
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

PS1='\w \e[34m->\e[0m '
