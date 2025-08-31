export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="simplerich"

# ZSH_THEME_RANDOM_CANDIDATES=( "muse" "aussiegeek" "bira" "candy" "crunch" "dst" "frisk" "macovsky" "mikeh" "murilasso" "simonoff" "steeef" "zhann" )

# install theme from this repo: https://github.com/philip82148/simplerich-zsh-theme
# source ~/simplerich-zsh-theme/zsh-git-prompt/zshrc.sh

# CASE_SENSITIVE="true"

# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
# zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# DISABLE_LS_COLORS="true"

# DISABLE_AUTO_TITLE="true"

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
alias add='sudo apt-fast install'
alias die='sudo aptitude remove'
alias scavenge='apt search'
alias update='sudo apt update && sudo apt upgrade && flatpak update && pipx upgrade-all && brew update && brew upgrade'
alias havei='aptitude search' # need to update eventually
# flatpak
alias fladd='flatpak install'
alias flbegone='flatpak remove'
# system
alias reboot='systemctl reboot'
alias poweroff='systemctl poweroff'
# misc
unalias gg
alias gg='exit' 
alias bat='batcat'
unalias _
unalias egrep
unalias fgrep
