import pandas as pd

# 尝试导入 yfinance 库用于数据下载，如果未安装则设置为 None
try:
    import yfinance as yf
except ImportError:  # pragma: no cover - yfinance 可能在测试环境中未安装
    yf = None


def fetch(symbol: str, start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """使用 yfinance 下载指定标的的历史数据。

    Parameters
    ----------
    symbol : str
        要下载的股票代码，例如 ``AAPL``。
    start : str, optional
        开始日期，格式 ``YYYY-MM-DD``。
    end : str, optional
        结束日期，格式 ``YYYY-MM-DD``。

    Returns
    -------
    pandas.DataFrame
        以日期为索引，包含 ``Close`` 收盘价列的 DataFrame。
    """
    if yf is None:
        raise ImportError(
            "yfinance 模块未安装，无法自动下载数据。请通过 'pip install yfinance' 安装。"
        )

    data = yf.download(symbol, start=start, end=end, progress=False)
    if 'Adj Close' in data.columns:
        data = data.rename(columns={'Adj Close': 'Close'})
    return data[['Close']]
