import tkinter as tk


class DummyButton(tk.Frame):

    # TODO: Simple plot
    # RSI, multiple windows, etc
    def __init__(self, parentFrame, controller):
        # wtf graphwdiget object has no attribute tk
        super(DummyButton, self).__init__(parentFrame)
        # TODO: Text box top left to control what ticker
        # Also indicator buttons
        self.controller = controller
        button = tk.Button(self, text="X--",
                           command=lambda: print("F"))
        button.pack(side="top", fill="both", expand=True)
