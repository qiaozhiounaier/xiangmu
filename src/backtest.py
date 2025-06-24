"""Backwards-compatible script for running a moving-average backtest on a CSV.

兼容旧用法的脚本，可在提供的 CSV 数据上运行均线交叉回测。
"""

from __future__ import annotations

import argparse
import pandas as pd

from .strategy import MovingAverageCrossStrategy
from .backtester import Backtester
from .plotting import plot


def moving_average_crossover(data: pd.DataFrame, short_window: int = 40, long_window: int = 100):
    """在给定数据上运行均线交叉回测。"""

    # 创建策略实例并执行回测
    strategy = MovingAverageCrossStrategy(short_window=short_window, long_window=long_window)
    bt = Backtester(strategy)
    return bt.run(data)


def main() -> None:
    parser = argparse.ArgumentParser(description='Simple moving average backtester')
    parser.add_argument('csv_file', help='CSV file with Date and Close columns')
    parser.add_argument('--short', type=int, default=40, help='Short moving average window')
    parser.add_argument('--long', type=int, default=100, help='Long moving average window')
    parser.add_argument('--output', help='Path to save the plot (PNG)')
    args = parser.parse_args()

    # 读取 CSV 数据，并将日期列设置为索引
    df = pd.read_csv(args.csv_file, parse_dates=['Date'])
    df.set_index('Date', inplace=True)

    # 执行回测
    result = moving_average_crossover(df, short_window=args.short, long_window=args.long)
    # 绘制并保存结果图表
    plot(df, result, save_path=args.output)


if __name__ == '__main__':
    main()

