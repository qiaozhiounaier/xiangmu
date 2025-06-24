from __future__ import annotations

import pandas as pd
from dataclasses import dataclass

from .strategy import Strategy


@dataclass
class BacktestResult:
    portfolio: pd.Series
    trades: pd.DataFrame


class Backtester:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def run(self, data: pd.DataFrame) -> BacktestResult:
        data = data.copy()
        signals = self.strategy.generate_signals(data)
        data['position'] = signals.shift(1).fillna(0)
        data['returns'] = data['Close'].pct_change().fillna(0)
        data['strategy'] = data['returns'] * data['position']
        portfolio = (1 + data['strategy']).cumprod()
        trades = data.loc[data['position'].diff() != 0, ['position']]
        return BacktestResult(portfolio=portfolio, trades=trades)
