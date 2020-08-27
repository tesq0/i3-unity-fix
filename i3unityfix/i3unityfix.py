#!/usr/bin/env python3

from i3ipc import Connection, Event
from pynput.keyboard import Key, Controller
import subprocess

def window_is_unity(window):
    if (window is None):
        return False
    return window.window_class == "Unity"

class I3UnityFix(object):

    def __init__(self):
        self.keyboard = Controller()
        
    def on_workspace_focus(self, i3, event):
        workspace = event.current

        windows = list(workspace.leaves())
        windows = filter(window_is_unity, windows)

        for window in windows:
            window.command("fullscreen enable")
            window.command("fullscreen disable")
            self.keyboard.press(Key.esc)
            self.keyboard.release(Key.esc)
            
def main():
    i3 = Connection()
    handler = I3UnityFix()
    i3.on(Event.WORKSPACE_FOCUS, handler.on_workspace_focus)
    i3.main()
    
if __name__ == "__main__":
    main()
