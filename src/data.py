import pandas as pd

try:
    import yfinance as yf
except ImportError:  # pragma: no cover - yfinance might not be installed in tests
    yf = None


def fetch(symbol: str, start: str | None = None, end: str | None = None) -> pd.DataFrame:
    """Fetch historical data for a symbol using yfinance.

    Parameters
    ----------
    symbol : str
        The ticker symbol to download, e.g. 'AAPL'.
    start : str, optional
        Start date in 'YYYY-MM-DD' format.
    end : str, optional
        End date in 'YYYY-MM-DD' format.

    Returns
    -------
    pandas.DataFrame
        DataFrame indexed by date with a `Close` column.
    """
    if yf is None:
        raise ImportError("yfinance is required for data download. Please install it via 'pip install yfinance'.")

    data = yf.download(symbol, start=start, end=end, progress=False)
    if 'Adj Close' in data.columns:
        data = data.rename(columns={'Adj Close': 'Close'})
    return data[['Close']]
