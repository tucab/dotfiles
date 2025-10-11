export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="simplerich"

# ZSH_THEME_RANDOM_CANDIDATES=( "muse" "aussiegeek" "bira" "candy" "crunch" "dst" "frisk" "macovsky" "mikeh" "murilasso" "simonoff" "steeef" "zhann" )

# install theme from this repo: https://github.com/philip82148/simplerich-zsh-theme
source ~/simplerich-zsh-theme/zsh-git-prompt/zshrc.sh

# CASE_SENSITIVE="true"

# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
zstyle ':omz:update' mode auto # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# DISABLE_LS_COLORS="true"

DISABLE_AUTO_TITLE="true"

ENABLE_CORRECTION="true"

# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"
plugins=(git)

source $ZSH/oh-my-zsh.sh

# ALIASES

# package management
alias gets='sudo emerge --ask --verbose'
alias chomp='sudo emerge --depclean'
alias query='emerge --pretend'
alias havei='sudo equery | grep'
alias update='sudo emerge --sync && sudo emerge --update --deep @world && brew update && brew upgrade'
# misc
unalias gg
alias gg='exit'
unalias _
unalias ls
alias ls='eza --icons=never --color=always'
alias fastfetch2='fastfetch --config examples/16.jsonc'
alias n='nvim'

source /usr/share/zsh/site-functions/zsh-syntax-highlighting.zsh
export PATH="$HOME/.config/emacs/bin:$PATH"
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
export COLORTERM=truecolor
export EDITOR="nvim"
export VISUAL="$EDITOR"
export PATH="$PATH:/home/juno/.local/bin"
