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

git_current_branch() {
    git rev-parse --abbrev-ref HEAD 2>/dev/null
}


bind 'set completion-ignore-case on'
bind 'set show-all-if-ambiguous on'
bind 'TAB:menu-complete'

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
export EDITOR="nvim"
export VISUAL="$EDITOR"
export PATH="$PATH:/home/juno/.local/bin"
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
eval "$(starship init bash)"
