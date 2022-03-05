#!/usr/bin/env python

from stock_analysis import StockReader
from stock_analysis import StockVisualizer
import matplotlib.pyplot as plt


def main():
    reader = StockReader('2020-01-01', '2020-12-31')

    # get bitcoin data in USD
    bitcoin = reader.get_bitcoin_data('USD')

    # get faang data
    fb, aapl, amzn, nflx, goog = (
        reader.get_ticker_data(ticker) \
        for ticker in ['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOG']
    )

    # get S&P 500 data
    sp = reader.get_index_data('S&P 500')

    netflix_viz = StockVisualizer(nflx)

    ax = netflix_viz.candlestick(
        date_range=None,
        resample=None,
        volume=False,
        figsize=(10, 4),
        title='Netflix closing price over time'
    )

    netflix_viz.add_reference_line(
        ax,
        x=nflx.high.idxmax(),
        color='k',
        linestyle=':',
        label=f'highest value ({nflx.high.idxmax():%b %d})',
        alpha=0.5
    )

    ax.set_ylabel('price ($)')

    plt.show()


if __name__ == "__main__":
    main()
