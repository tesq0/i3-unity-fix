#!/usr/bin/env python3

from i3ipc import Connection, Event
from pynput.keyboard import Key, Controller
import subprocess

def window_is_unity(window):
    if (window is None):
        return False
    return window.window_class == "Unity"

def find_focused_window(container):

    while container:
        if not hasattr(container, 'focus') or not container.focus:
            break

        container_id = container.focus[0]
        container = container.find_by_id(container_id)
    
    return container;
        

class I3UnityFix(object):

    def __init__(self):
        self.keyboard = Controller()
        
    def on_workspace_focus(self, i3, event):

        if event.old.name == "__i3_scratch":
            return
            
        workspace = event.current

        # Same screen check
        if event.old.rect.x == event.current.rect.x:
            windows = list(workspace.leaves())
            windows = list(filter(window_is_unity, windows))

            previously_focused_window = None

            if len(windows) > 1:
                previously_focused_window = find_focused_window(workspace)

            for window in windows:
                window.command("fullscreen enable")
                window.command("fullscreen disable")
                self.keyboard.press(Key.home)
                self.keyboard.release(Key.home)

            if previously_focused_window is not None and previously_focused_window.window_class == "Unity":
                previously_focused_window.command("focus")
        
	
            
def main():
    i3 = Connection()
    handler = I3UnityFix()
    i3.on(Event.WORKSPACE_FOCUS, handler.on_workspace_focus)
    i3.main()
    
if __name__ == "__main__":
    main()
