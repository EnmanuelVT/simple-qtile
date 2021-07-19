#!/bin/bash

apropos . | dmenu -p MAN: -l 20 | awk '{print $1}' | xargs -r man -Tpdf | zathura -

