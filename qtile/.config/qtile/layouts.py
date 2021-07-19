from libqtile import layout
import json
colorscheme = json.load(open('/home/emmanuel/.config/qtile/theme.json', 'r'))

layouts = [
    layout.Max(),
    layout.MonadTall(
        border_focus=colorscheme["accent"],
        border_width=2,
        margin=8,
        new_at_current=False,
    ),
    # layout.Stack(
    #     border_focus=colorscheme["accent"],
    #     margin=8,
    #     border_width=2,
    # ),
    # layout.Bsp(
    #     border_focus=colorscheme["accent"],
    #     margin=8,
    # ),
    layout.floating.Floating(
        border_focus=colorscheme["accent"],
    ),
]
