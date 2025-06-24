"""Minimal quantitative trading backtesting framework."""
"""极简的量化交易回测框架。"""

from .data import fetch
from .strategy import Strategy, MovingAverageCrossStrategy
from .backtester import Backtester, BacktestResult
from .plotting import plot

__all__ = [
    'fetch',
    'Strategy',
    'MovingAverageCrossStrategy',
    'Backtester',
    'BacktestResult',
    'plot',
]
