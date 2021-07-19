#!/bin/bash
cd "$(dirname "$(readlink -f "$0")")"

help () {
  echo -e "Available themes:\\n $(fd . ./themes | awk -F/ '{print $NF}')"
}

case $1 in
  help|-h|--help|'')
    help
    exit;;
esac

theme=$(fd $1 ./themes)
if [ -z $theme ]; then
  echo "Theme $1 not found."
  exit 1
fi
ln -sf $theme ./theme.json
qtile cmd-obj -o cmd -f restart

