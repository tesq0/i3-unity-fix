#!/usr/bin/env python3

from i3ipc import Connection, Event
from pynput.keyboard import Key, Controller
import subprocess

class I3UnityFix(object):

    def __init__(self):
        self.keyboard = Controller()
    
    def on_focus(self, i3, event):
        if (event.container.window_class == "Unity"):
            event.container.command("fullscreen enable")
            event.container.command("fullscreen disable")
            self.keyboard.press(Key.space)
            self.keyboard.release(Key.space)
            
def main():
    i3 = Connection()
    handler = I3UnityFix()
    i3.on(Event.WINDOW_FOCUS, handler.on_focus)
    i3.main()
    
if __name__ == "__main__":
    main()
