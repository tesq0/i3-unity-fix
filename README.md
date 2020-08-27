Fixes unity3d editor repaint issue when switching workspaces in the i3 window manager

# About

When switching workspaces in i3 to a workspace that has a unity3d window open, the editor won't repaint its contents and display artifacts from the previous workspace.
I found out that toggling the fullscreen mode on and off forces the unity window to repaint and somewhat fixes the problem.
This script does exactly that.

# Dependencies

i3ipc

# Usage

Tell i3 to start the script in the i3 config file

exec --no-startup-id /path/to/i3unityfix.py &

