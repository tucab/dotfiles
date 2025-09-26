# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import subprocess
import os
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

catppuccin_colors = {
    "rosewater": "#f4dbd6",
    "flamingo": "#f0c6c6",
    "pink": "#f5bde6",
    "mauve": "#c6a0f6",
    "red": "#ed8796",
    "peach": "#f5a97f",
    "yellow": "#eed49f",
    "green": "#a6da95",
    "teal": "#8bd5ca",
    "sky": "#91d7e3",
    "sapphire": "#7dc4e4",
    "blue": "#8aadf4",
    "lavender": "#b7bdf8",
    "text": "#cad3f5",
    "subtext1": "#b8c0e0",
    "subtext0": "#a5adcb",
    "overlay2": "#939ab7",
    "overlay1": "#8087a2",
    "overlay0": "#6e738d",
    "surface2": "#5b6078",
    "surface1": "#493d64",
    "surface0": "#363a4f",
    "base": "#24273a",
    "mantle": "#1e2030",
    "crust": "#181926",
}

os.system("feh --bg-scale ~/Pictures/bookmarks.png")

mod = "mod4"
terminal = "/usr/bin/kitty"
browser = "/usr/bin/firefox"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(["control", "mod1"], "t", lazy.spawn(terminal), desc="Launch terminal"),
    Key(["control", "shift"], "f", lazy.spawn(browser), desc="Launch browser"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key(["control", "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse sset Master 5%-"),
        desc="Lower volume by 5%",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse sset Master 5%+"),
        desc="Raise volume by 5%",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -D pulse sset Master toggle"),
        desc="Mute/Unmute Volume",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause player",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Skip to next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Skip to previous"),
    Key([mod, "control", "shift"], "l", lazy.spawn("i3lock -c 24273a"), desc="Lock screen"),
    Key([mod], "d", lazy.spawn("rofi -show run"), desc="Launch rofi"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [
    Group("1"),
    Group("2"),
    Group("3", matches=[Match(wm_class=["vesktop"])]),
    Group("4"),
    Group("5"),
    Group("6"),
    Group("7"),
    Group("8"),
    Group("9"),
]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Bsp(
        border_focus=catppuccin_colors["lavender"],
        border_normal=catppuccin_colors["crust"],
        border_width=2,
        margin=1,
        ratio=1.5,
        wrap_clients=True,
        border_on_single=True,
    ),
    # layout.Plasma(
    #     border_focus=catppuccin_colors["lavender"],
    #     border_normal=catppuccin_colors["crust"],
    #     border_width=2,
    #     margin=1,
    # ),
    layout.Max(
        border_focus=catppuccin_colors["lavender"],
        border_normal=catppuccin_colors["crust"],
        border_width=2,
        margin=1,
    ),
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    layout.MonadTall(
        border_focus=catppuccin_colors["lavender"],
        border_focus_fixed=catppuccin_colors["lavender"],
        border_normal=catppuccin_colors["crust"],
        border_normal_fixed=catppuccin_colors["crust"],
        border_width=2,
        margin=1,
        max_ratio=0.8,
        min_ratio=0.2,
    ),
    # layout.MonadWide(),
    # layout.RatioTile(
    #     border_focus=catppuccin_colors["lavender"],
    #     border_normal=catppuccin_colors["crust"],
    #     border_width=2,
    #     margin=1,
    #     fancy=True,
    #     ratio=1.5,
    # ),
    # layout.Tile(),
    # layout.TreeTab(
    #    active_bg=catppuccin_colors["crust"],
    #    active_fg=catppuccin_colors["text"],
    #    bg_color=catppuccin_colors["base"],
    #    inactive_bg=catppuccin_colors["mantle"],
    #    inactive_fg=c
    #    panel_width=100,
    # ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
                widget.Sep(
                    foreground=catppuccin_colors["overlay1"],
                    padding=3,
                    size_percent=75,
                ),
                widget.GroupBox(
                    active=catppuccin_colors["lavender"],
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                    highlight_method="line",
                    disable_drag=True,
                    this_current_screen_border=catppuccin_colors["lavender"],
                    this_screen_border=catppuccin_colors["lavender"],
                    borderwidth=3,
                    inactive=catppuccin_colors["overlay1"],
                    use_mouse_wheel=False,
                    urgent_border=catppuccin_colors["rosewater"],
                    urgent_text=catppuccin_colors["rosewater"],
                ),
                widget.Sep(
                    foreground=catppuccin_colors["overlay1"],
                    padding=3,
                    size_percent=75,
                ),
                widget.Prompt(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
                widget.WindowName(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
                widget.Spacer(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["base"],
                    length=bar.STRETCH,
                ),
                widget.Clock(
                    format="%d %b %Y %a %H:%M:%S",
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
                widget.Spacer(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["base"],
                    length=bar.STRETCH,
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
                widget.Sep(
                    foreground=catppuccin_colors["overlay1"],
                    padding=5,
                    size_percent=75,
                ),
                widget.Volume(
                    fmt="{} ",
		            unmuted_format="{char} {volume}%",
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                    emoji=True,
                    emoji_list=["", "", "", ""],
                ),
                widget.Sep(
                    foreground=catppuccin_colors["overlay1"],
                    padding=3,
                    size_percent=75,
                ),
                widget.Battery(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                    format="{char} {percent:1.0%}",
                    charge_char="󰂏",
                    discharge_char="󰂌",
                    empty_char="󰂎",
                    full_char="󰁹",
                    not_charging_char="󰂃",
                    unknown_char="󰂑",
                ),
                widget.Sep(
                    foreground=catppuccin_colors["overlay1"],
                    padding=3,
                    size_percent=75,
                ),
                widget.QuickExit(
                    background=catppuccin_colors["base"],
                    foreground=catppuccin_colors["text"],
                ),
            ],
            30,
            background=catppuccin_colors["mantle"],
            border_width=[2, 2, 2, 2],  # Draw top and bottom borders
            border_color=[
                catppuccin_colors["lavender"],
                catppuccin_colors["lavender"],
                catppuccin_colors["lavender"],
                catppuccin_colors["lavender"],
            ],
            margin=[2, 1, 0, 1],
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call(home)

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
