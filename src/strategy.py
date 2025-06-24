from __future__ import annotations

import pandas as pd


class Strategy:
    """策略基类。"""

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """返回持仓信号 (1 做多，-1 做空，0 空仓)。"""
        raise NotImplementedError


class MovingAverageCrossStrategy(Strategy):
    """简单的均线交叉策略。"""

    def __init__(self, short_window: int = 40, long_window: int = 100):
        # 短期和长期均线窗口
        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        # 复制数据以便计算均线
        df = data.copy()
        df['short_ma'] = df['Close'].rolling(self.short_window, min_periods=1).mean()
        df['long_ma'] = df['Close'].rolling(self.long_window, min_periods=1).mean()
        signals = pd.Series(0, index=df.index)
        signals[df['short_ma'] > df['long_ma']] = 1
        signals[df['short_ma'] < df['long_ma']] = -1
        # 将均线回写到原始数据，方便后续绘图
        data['short_ma'] = df['short_ma']
        data['long_ma'] = df['long_ma']
        return signals
