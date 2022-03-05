import tkinter as tk
from tkinter import messagebox

import datetime

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import mplfinance as mpf

from src.gfx.Utils import destroyRecursively
from stock_analysis import StockReader
from stock_analysis import StockVisualizer
from src.gfx.GraphWidget.MenuBar import MenuBar


class GraphWidget(tk.Frame):

    # TODO: Simple plot
    # RSI, multiple windows, etc
    def __init__(self, parentFrame, controller):
        # wtf graphwdiget object has no attribute tk
        super(GraphWidget, self).__init__(parentFrame)
        self.graphRoot = None
        self.curChart = None
        self.controller = controller

        self.menuFrame = MenuBar(self, controller)
        self.menuFrame.pack(side="top", fill="both", expand=False)

        '''
        # TODO: Text box top left to control what ticker
        # Also indicator buttons
        self.controller = controller
        button = tk.Button(self, text="X--",
                           command=lambda: print("F"))

        button.pack(side="top", fill="both", expand=True)
        '''

    def handleTickerQuery(self, ticker: str, interval: str):
        try:
            self.handleTickerQueryHelper(ticker, interval)
        except Exception as e:
            messagebox.showerror("Error getting ticker", e)

    # Defaults back to 20 units backwords
    def handleTickerQueryHelper(self, ticker: str, interval: str):
        lookBackPeriod = 10
        print(ticker)
        curTime = datetime.datetime.now()
        prevTime = curTime - (datetime.timedelta(days=lookBackPeriod) if str == "D" else (
            datetime.timedelta(days=7 * lookBackPeriod) if str == "W" else datetime.timedelta(
                days=31 * lookBackPeriod)))

        curTime = str(curTime.date())

        prevTime = str(prevTime.date())

        reader = StockReader(prevTime, curTime)
        vis = StockVisualizer(reader.get_ticker_data(ticker))


        # Theme customization
        mc = mpf.make_marketcolors(up='#00ff00', down='#ff0000', inherit=True)
        s = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=mc)

        fig, _ = vis.candlestick(
            date_range=None,
            resample=None,
            volume=True,
            figscale=1.8,
            returnfig=True,
            # title=f'{ticker} chart from {prevTime} to {curTime}',
            style=s
        )
        fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)

        if self.graphRoot is not None:
            destroyRecursively(self.graphRoot)

        # Generate frame for tkinter
        # Make a top level window
        self.graphRoot = tk.Frame(self)
        self.graphRoot.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        self.graphRoot.columnconfigure(0, weight=0)
        self.graphRoot.columnconfigure(1, weight=1)
        self.graphRoot.columnconfigure(2, weight=0)
        self.graphRoot.rowconfigure(0, weight=9)
        self.graphRoot.rowconfigure(1, weight=2)

        self.graphRootChart = tk.Frame(self.graphRoot)
        self.graphRootChart.grid(row=0, column=1, sticky="nsew")
        self.graphTKChart = tk.Frame(self.graphRoot)
        self.graphTKChart.grid(row=1, column=1, sticky="nsew")

        # Add a canvas containing the figure
        canvas = FigureCanvasTkAgg(fig, self.graphRootChart)
        # Draw it
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=False)

        toolbar = NavigationToolbar2Tk(canvas, self.graphTKChart)
        toolbar.update()
        toolbar.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False)
