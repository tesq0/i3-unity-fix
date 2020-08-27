#!/usr/bin/env python3

from i3ipc import Connection, Event
from time import sleep
import subprocess

class I3UnityFix(object):
    
    def on_focus(self, i3, event):
        if (event.container.window_class == "Unity"):
            event.container.command("fullscreen enable")
            event.container.command("fullscreen disable")
            
def main():
    i3 = Connection()
    handler = I3UnityFix()
    i3.on(Event.WINDOW_FOCUS, handler.on_focus)
    i3.on(Event.WORKSPACE, handler.on_workspace)
    i3.main()
    
if __name__ == "__main__":
    main()
