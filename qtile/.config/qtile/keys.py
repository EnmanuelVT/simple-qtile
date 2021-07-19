import json

from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from libqtile import extension

from progs import *

colorscheme = json.load(open('/home/emmanuel/.config/qtile/theme.json', 'r'))

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Focus left window"),
    Key([mod], "l", lazy.layout.right(), desc="Focus right window"),
    Key([mod], "j", lazy.layout.down(), desc="Focus down window"),
    Key([mod], "k", lazy.layout.up(), desc="Focus up window"),

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "space", lazy.layout.flip(), desc="Flip windows"),
    Key([mod, "control"], "space", lazy.layout.rotate(), desc="Rotate windows"),

    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),

    Key([mod, "control"], "j", lazy.layout.grow_down()),
    Key([mod, "control"], "k", lazy.layout.grow_up()),
    Key([mod, "control"], "h", lazy.layout.grow_left()),
    Key([mod, "control"], "l", lazy.layout.grow_right()),

    Key([mod], "i", lazy.layout.grow(), desc="Grow window"),
    Key([mod], "m", lazy.layout.shrink(), desc="Shrink window"),
    Key([mod], "n", lazy.layout.normalize(), desc="Normalize window"),
    Key([mod], "o", lazy.layout.maximize(), desc="Maximize window"),

    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),
    Key(["mod1"], "Tab", lazy.layout.up(),
        desc="Switch window focus to other pane(s) of stack"),
    Key(["mod1", "shift"], "Tab", lazy.layout.down(),
        desc="Switch window focus to other pane(s) of stack"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Next layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Previous layout"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "b", lazy.hide_show_bar(), desc="Toggle bar"),

    Key([mod], "f", lazy.window.toggle_floating(), desc="Toggle floating"),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen"),
    Key([mod, "control"], "f", lazy.window.toggle_maximize(),
        desc="Toggle maximize"),
    Key([mod], "Escape", lazy.window.toggle_minimize(),
        desc="Toggle minimize"),
    Key([mod, "shift"], "Escape", lazy.group.unminimize_all(),
        desc="Unminimize all"),

    Key([mod], "e", lazy.spawn(explorer), desc="Spawn explorer"),

    KeyChord([mod], "a", [
        Key([], "o", lazy.spawn(office), desc="Spawn office"),
        Key([], "b", lazy.spawn(browser), desc="Spawn browser"),
        Key(["shift"], "b", lazy.spawn(browser + ' --private-window --incognito'),
            desc="Spawn incognito browser"),
        Key([], "e", lazy.spawn(explorer), desc="Spawn explorer"),
        Key([], "s", lazy.spawn("quick-search.sh"), desc="Spawn quick search"),
        Key([], "f", lazy.spawn("dmfav.sh"),
            desc="Spawn favorite websites"),
        Key([], "m", lazy.spawn("launchman.sh"),
            desc="Launchman"),
        Key([], "n", lazy.spawn("nitrogen --random --set-scaled"),
            desc="Set background"),
        Key([], "c", lazy.spawn("bc-dmenu.sh"),
            desc="Spawn dmenu calculator"),

        Key([mod], "o", lazy.spawn(office), desc="Spawn office"),
        Key([mod], "b", lazy.spawn(browser), desc="Spawn browser"),
        Key([mod, "shift"], "b", lazy.spawn(browser + ' --private-window --incognito'),
            desc="Spawn incognito browser"),
        Key([mod], "e", lazy.spawn(explorer), desc="Spawn explorer"),
        Key([mod], "s", lazy.spawn("quick-search.sh"), desc="Spawn quick search"),
        Key([mod], "f", lazy.spawn("dmfav.sh"),
            desc="Spawn favorite websites"),
        Key([mod], "m", lazy.spawn("launchman.sh"),
            desc="Launchman"),
        Key([mod], "n", lazy.spawn("nitrogen --set-scaled"),
            desc="Set background"),
        Key([mod], "c", lazy.spawn("bc-dmenu.sh"),
            desc="Spawn dmenu calculator"),
    ]),

    Key([mod], "c", lazy.run_extension(extension.WindowList(
        font="Ubuntu Nerd Font",
        dmenu_ignorecase=True,
        dmenu_command='dmenu -nb ' + colorscheme["background"] + ' -nf ' +
        colorscheme["foreground"] + ' -sb ' +
        colorscheme["accent"] + ' -p WINDOW:',
        item_format='{group} {window} {id}',
    )), desc="Spawn dmenu window switcher"),

    Key([mod, "shift"], "r", lazy.run_extension(extension.J4DmenuDesktop(
        dmenu_prompt="APP:",
        dmenu_ignorecase=True,
        dmenu_font="Roboto-10",
        background=colorscheme["background"],
        foreground=colorscheme["foreground"],
        selected_background=colorscheme["accent"],
        selected_foreground=colorscheme["foreground"],
        j4dmenu_terminal=terminal,
    )), desc="Spawn dmenu desktop"),

    Key([mod], "r", lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="RUN:",
        dmenu_font="Roboto-10",
        background=colorscheme["background"],
        foreground=colorscheme["foreground"],
        selected_background=colorscheme["accent"],
        selected_foreground=colorscheme["foreground"],
    )), desc="Spawn a command using a prompt widget"),

    Key([mod], "Up", lazy.layout.up(), desc="Focus up window"),
    Key([mod], "Down", lazy.layout.down(), desc="Focus down window"),
    Key([mod], "Right", lazy.screen.next_group(), desc="Next group"),
    Key([mod], "Left", lazy.screen.prev_group(), desc="Prev group"),
    Key([mod, "control"], "n", lazy.screen.next_group(), desc="Next group"),
    Key([mod, "control"], "p", lazy.screen.prev_group(), desc="Prev group"),

    Key([mod], 'F1', lazy.spawn("qtile_switch_theme.sh emmanuel")),
    Key([mod], 'F2', lazy.spawn("qtile_switch_theme.sh gruvbox")),
    # toggle visibiliy of Dropdowns
    Key([mod], 'F11', lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], 'F12', lazy.group['scratchpad'].dropdown_toggle('htop')),

    Key([mod], "s", lazy.spawn(screenshooter), desc="Launch screenshooter"),
    Key([], "XF86TouchpadToggle", lazy.spawn(
        "touchpad_toggle.sh"), desc="Toggle touchpad"),
    Key([mod], "Print", lazy.spawn(screenshooter), desc="Launch screenshooter"),

    Key([mod], "period", lazy.spawn(emoji_keyboard),
        desc="Launch emoji_keyboard"),

    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pulseaudio-ctl up"), desc="Volume up"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pulseaudio-ctl down"), desc="Volume down"),
    Key([], "XF86AudioMute", lazy.spawn(
        "pulseaudio-ctl mute"), desc="Volume mute"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "xbacklight-ctl up"), desc="Increase backlight"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "xbacklight-ctl down"), desc="Decrease backlight"),
    Key(["shift"], "XF86MonBrightnessUp", lazy.spawn(
        "xbacklight-ctl max"), desc="Set max backlight"),
    Key(["shift"], "XF86MonBrightnessDown", lazy.spawn(
        "xbacklight-ctl min"), desc="Set min backlight"),

    Key([mod, "control"], "l", lazy.spawn(logout), desc="Spawn logout prompt"),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
]
