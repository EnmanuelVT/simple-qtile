#!/bin/bash

cd ~/.dotfiles
./.update_installed.sh

git add .
git commit -m "$(date)"
git push
