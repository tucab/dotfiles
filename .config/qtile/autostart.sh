#!/bin/sh
picom --config ~/.config/picom/picom.conf &
setxkbmap -option caps:swapescape &
dunst &
emacs --daemon &
kdeconnectd &
pulseaudio --start &
