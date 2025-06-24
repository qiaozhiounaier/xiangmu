from __future__ import annotations

import argparse
import pandas as pd

from . import data as data_module
from .strategy import MovingAverageCrossStrategy
from .backtester import Backtester
from .plotting import plot


def load_data(args: argparse.Namespace) -> pd.DataFrame:
    if args.csv:
        df = pd.read_csv(args.csv, parse_dates=['Date'])
        df.set_index('Date', inplace=True)
        return df
    return data_module.fetch(args.symbol, start=args.start, end=args.end)


def main() -> None:
    parser = argparse.ArgumentParser(description='Run moving average backtest')
    parser.add_argument('--symbol', default='AAPL', help='Ticker symbol to download')
    parser.add_argument('--start', help='Start date YYYY-MM-DD')
    parser.add_argument('--end', help='End date YYYY-MM-DD')
    parser.add_argument('--csv', help='Instead of downloading, read data from this CSV file')
    parser.add_argument('--short', type=int, default=40, help='Short moving average window')
    parser.add_argument('--long', type=int, default=100, help='Long moving average window')
    parser.add_argument('--output', help='Path to save the plot (PNG)')
    args = parser.parse_args()

    df = load_data(args)
    strategy = MovingAverageCrossStrategy(short_window=args.short, long_window=args.long)
    bt = Backtester(strategy)
    result = bt.run(df)
    plot(df, result, save_path=args.output)


if __name__ == '__main__':
    main()
