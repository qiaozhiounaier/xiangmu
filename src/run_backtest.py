from __future__ import annotations

import argparse
import pandas as pd

from . import data as data_module
from .strategy import MovingAverageCrossStrategy
from .backtester import Backtester
from .plotting import plot


def load_data(args: argparse.Namespace) -> pd.DataFrame:
    """根据参数加载数据，优先读取本地 CSV。"""

    if args.csv:
        df = pd.read_csv(args.csv, parse_dates=['Date'])
        df.set_index('Date', inplace=True)
        return df
    # 若未指定 CSV，则通过 yfinance 下载数据
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

    # 加载数据
    df = load_data(args)
    # 初始化策略与回测器
    strategy = MovingAverageCrossStrategy(short_window=args.short, long_window=args.long)
    bt = Backtester(strategy)
    # 执行回测并绘图
    result = bt.run(df)
    plot(df, result, save_path=args.output)


if __name__ == '__main__':
    main()
