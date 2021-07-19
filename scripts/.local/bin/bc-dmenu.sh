#!/bin/bash

result=$(dmenu | bc)

[ -z $result ] && exit

notify-send -i /usr/share/icons/Flatery-Dark/apps/32/accessories-calculator.svg -u low -t 1000 "Result '$result' copied to clipboard."
echo $result | xclip -selection clipboard
