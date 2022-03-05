import tkinter as tk

# Root window
from src.gfx.GraphWidget.GraphWidget import GraphWidget


class MainWindow(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.sideFrame = None
        self.rootFrame = None
        self.mainFrame = None
        self.frames = {}
        self.setup(name)

    def setup(self, name):
        # Set title
        self.title(name)
        # Maximize
        self.geometry("%dx%d+0+0" % (super().winfo_screenwidth(), super().winfo_screenheight()))

        # Root frame
        self.rootFrame = tk.Frame(self, highlightbackground="black", highlightthickness=2)
        self.rootFrame.pack(side="top", fill="both", expand=True)

        # Root frame should take up everything
        self.rootFrame.grid_rowconfigure(0, weight=1)
        self.rootFrame.grid_columnconfigure(0, weight=1)
        self.rootFrame.grid_columnconfigure(1, weight=9)

        # Left frame side info(TODO: make minimizable)
        self.sideFrame = tk.Frame(self.rootFrame, highlightbackground="red", highlightthickness=2)
        self.sideFrame.grid(row=0, column=0, sticky="nsew")
        self.sideFrame.grid_rowconfigure(0, weight=1)
        self.sideFrame.grid_columnconfigure(0, weight=1)

        # Main frame (80-90 % right side)
        self.mainFrame = tk.Frame(self.rootFrame, highlightbackground="blue", highlightthickness=2)
        self.mainFrame.grid(row=0, column=1, sticky="nsew")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)

        moduleFrames = [GraphWidget]

        # Add Widgets/Frames
        for F in moduleFrames:
            frame = F(self.mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        '''
        G2 = GraphWidget(self.sideFrame, self)
        frame.grid(row=0, column=, sticky="nsew")
        # place a button on the root window
        tk.Button(self,
                  text='X',
                  command=self.destroy).pack(fill=tk.X, side=tk.RIGHT, anchor=tk.NE)
        '''

    def show_frame(self, cont):
        self.frames[cont].tkraise()

    def destory_frame(self, frm: tk.Frame):
        frm.pack_forget()
        frm.grid_forget()
        frm.destroy()
