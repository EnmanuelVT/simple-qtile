#!/bin/bash

picom --experimental-backends &
zvuchno &
xset r rate 280 50 &
xsetroot -cursor_name left_ptr &
dex -a -s /etc/xdg/autostart/:~/.config/autostart/ &
