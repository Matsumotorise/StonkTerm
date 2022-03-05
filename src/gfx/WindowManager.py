import tkinter as tk

import os
from src.gfx.MainWindow import MainWindow


class WindowManager():
    def __init__(self, name):
        self.window = MainWindow(name)

        #self.window.tk.call("source", "assets/Azure-ttk-theme-2.1.0/azure.tcl")
        #self.window.tk.call("set_theme", "dark")

    def start(self):
        self.window.mainloop()

    def change_themes(self):
        # NOTE: The theme's real name is azure-<mode>
        if self.window.tk.call("ttk::style", "theme", "use") == "azure-dark":
            # Set light theme
            self.window.tk.call("set_theme", "light")
        else:
            # Set dark theme
            self.window.tk.call("set_theme", "dark")