from src.gfx.WindowManager import WindowManager

from stock_analysis import StockReader
from stock_analysis import StockVisualizer


def main():
    wm = WindowManager("StonkTerm")
    wm.start()


if __name__ == "__main__":
    main()
