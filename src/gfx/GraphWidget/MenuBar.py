import tkinter as tk

MENU_HEIGHT = 10


class MenuBar(tk.Frame):
    def __init__(self, parentFrame, controller):
        # wtf graphwdiget object has no attribute tk
        super(MenuBar, self).__init__(parentFrame)#,  highlightbackground="yellow", highlightthickness=2)
        self.controller = controller
        self.parentFrame = parentFrame
        paddings = {'padx': 2, 'pady': 5}

        self.tickerEntryBox = tk.Entry(self, width=7)
        self.tickerEntryBox.grid(row=0, column=0, sticky="nsew", **paddings)
        #self.tickerEntryBox.pack(side=tk.LEFT, anchor=tk.NW)
        self.tickerEntryBox.bind('<Return>', self.updateParent)


        intervals = ("D", "W", "M")

        self.intervalSelection = tk.StringVar(self)
        self.intervalSelection.set(intervals[0])
        self.timeIntervalMenu = tk.OptionMenu(self, self.intervalSelection,command =self.updateParent,  *intervals)
        #self.timeIntervalMenu.pack(side=tk.TOP, anchor=tk.N)
        self.timeIntervalMenu.grid(row=0, column=1, sticky="nsew", **paddings)

    def updateParent(self, event=None):
        print(self.tickerEntryBox.get())
        if self.tickerEntryBox.get() != "":
            self.parentFrame.handleTickerQuery(self.tickerEntryBox.get(), self.intervalSelection.get())