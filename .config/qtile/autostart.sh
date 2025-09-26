#!/bin/sh
picom --config ~/.config/picom/picom.conf &
setxkbmap -option caps:swapescape &
dunst &
kdeconnectd &
pulseaudio --start &
flameshot &
emacs --daemon
eval '$(dbus-launch --sh-syntax)'
