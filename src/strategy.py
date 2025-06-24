from __future__ import annotations

import pandas as pd


class Strategy:
    """Base strategy class."""

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """Return a Series of position signals (1 long, -1 short, 0 flat)."""
        raise NotImplementedError


class MovingAverageCrossStrategy(Strategy):
    """Simple moving-average crossover strategy."""

    def __init__(self, short_window: int = 40, long_window: int = 100):
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        df = data.copy()
        df['short_ma'] = df['Close'].rolling(self.short_window, min_periods=1).mean()
        df['long_ma'] = df['Close'].rolling(self.long_window, min_periods=1).mean()
        signals = pd.Series(0, index=df.index)
        signals[df['short_ma'] > df['long_ma']] = 1
        signals[df['short_ma'] < df['long_ma']] = -1
        # attach moving averages back to original frame for plotting
        data['short_ma'] = df['short_ma']
        data['long_ma'] = df['long_ma']
        return signals
