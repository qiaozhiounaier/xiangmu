import matplotlib.pyplot as plt
import pandas as pd

from .backtester import BacktestResult


def plot(data: pd.DataFrame, result: BacktestResult, save_path: str | None = None) -> None:
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    ax[0].plot(data['Close'], label='Close Price')
    if 'short_ma' in data:
        ax[0].plot(data['short_ma'], label='Short MA')
    if 'long_ma' in data:
        ax[0].plot(data['long_ma'], label='Long MA')
    ax[0].legend()
    ax[0].set_title('Price and Moving Averages')

    ax[1].plot(result.portfolio, label='Strategy Equity')
    ax[1].legend()
    ax[1].set_title('Portfolio Value')

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
