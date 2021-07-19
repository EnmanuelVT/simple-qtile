from libqtile.lazy import lazy
from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from keys import keys
from progs import mod

group_names = '1 2 3 4 5 6 7'.split()

groups = [
    ScratchPad("scratchpad", [
        # define a drop down terminal.
        # it is placed in the upper third of screen by default.
        DropDown("term", "alacritty -e fish", x=0.05, width=0.9, height=0.6),

        # define another terminal exclusively for qshell at different position
        DropDown("htop", "alacritty -e htop",
                 x=0.05, y=0.4, width=0.9, height=0.6,
                 on_focus_lost_hide=True)]),
    Group("1"),
    Group("2"),
    Group("3"),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
]
for i, name in enumerate(group_names):
    indx = str(i + 1)
    keys += [
        Key([mod], indx, lazy.group[name].toscreen()),
        Key([mod, 'shift'], indx, lazy.window.togroup(name))]
