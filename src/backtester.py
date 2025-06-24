from __future__ import annotations

import pandas as pd
from dataclasses import dataclass

from .strategy import Strategy


@dataclass
class BacktestResult:
    """回测结果结构体。"""

    portfolio: pd.Series
    trades: pd.DataFrame


class Backtester:
    """执行策略并生成回测结果的核心类。"""

    def __init__(self, strategy: Strategy):
        # 传入具体的交易策略对象
        self.strategy = strategy

    def run(self, data: pd.DataFrame) -> BacktestResult:
        """执行回测并返回结果。"""

        data = data.copy()
        # 生成买卖信号
        signals = self.strategy.generate_signals(data)
        # 根据信号计算持仓
        data['position'] = signals.shift(1).fillna(0)
        # 计算每日收益率
        data['returns'] = data['Close'].pct_change().fillna(0)
        # 策略收益 = 持仓 * 每日收益率
        data['strategy'] = data['returns'] * data['position']
        # 将收益累乘得到资金曲线
        portfolio = (1 + data['strategy']).cumprod()
        # 记录交易点
        trades = data.loc[data['position'].diff() != 0, ['position']]
        return BacktestResult(portfolio=portfolio, trades=trades)
