#!/bin/bash

# PROTOCOL
P='https'
WEBSITES="$P://youtube.com\\n$P://duckduckgo.com\\n$P://wiki.archlinux.org/\\n$P://web.whatsapp.com\\n$P://gmail.com\\n$P://classroom.google.com\\n$P://translate.google.com"

printf $WEBSITES | dmenu -l 30 -p 'FAV:' | xargs -r librewolf
