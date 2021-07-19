from widgets import widgets
from progs import mod
from keys import keys
from layouts import layouts
from groups import groups

from libqtile import bar, layout, widget, hook, extension, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Screen, Match
from libqtile.lazy import lazy
from typing import List

import os
import subprocess

import json

colorscheme = json.load(open('/home/emmanuel/.config/qtile/theme.json', 'r'))

widget_defaults = dict(
    font='Roboto',
    fontsize=12,
    padding=3,
    foreground=colorscheme["foreground"],
    background=colorscheme["background"],
)
extension_defaults = widget_defaults.copy()


screens = [
    Screen(
        top=bar.Bar(
            widgets,
            22,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='zoom'),
    Match(wm_class='florence'),
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(wm_class='dialog'),  # ssh-askpass
    Match(wm_class='toolbar'),  # ssh-askpass
    Match(wm_class='splash'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"


@ hook.subscribe.startup_once
def autostart():
    process = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([process])


@ hook.subscribe.startup
def startup():
    process = os.path.expanduser('~/.local/bin/fixcursor.sh')
    subprocess.call([process])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
