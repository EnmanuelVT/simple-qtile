from libqtile import widget, qtile
from libqtile import lazy
import json

colorscheme = json.load(open('/home/emmanuel/.config/qtile/theme.json', 'r'))


widgets = [
    widget.GroupBox(
        fontsize=20,
        highlight_method='line',
        padding_x=4,
        disable_drag=True,
        rounded=False,
        margin_x=0,
        inactive=colorscheme["inactive"],
        active=colorscheme["foreground"],
        this_current_screen_border=colorscheme["accent"],
        highlight_color=colorscheme["current"],
    ),

    widget.Spacer(),

    widget.CurrentLayoutIcon(
        background=colorscheme["secondary"],
        scale=0.8,
        mouse_callbacks={
            'Button4': lambda: qtile.cmd_next_layout(),
            'Button5': lambda: qtile.cmd_prev_layout()
        },
    ),
    widget.CurrentLayout(
        background=colorscheme["secondary"],
        mouse_callbacks={
            'Button4': lambda: qtile.cmd_next_layout(),
            'Button5': lambda: qtile.cmd_prev_layout()
        },
    ),

    widget.Clock(
        format='%Y-%m-%d %a %I:%M %p',
        background=colorscheme["accent"],
    ),
]
