# Quantitative Trading Infrastructure

This repository provides a small framework for downloading market data, running
backtests and visualising results. A moving average crossover strategy is
included as an example.

## Requirements
- Python 3.8+
- pandas
- matplotlib
- yfinance (for automatic data download)

Install dependencies with:

```bash
pip install pandas matplotlib yfinance
```

## Usage

### Fetch data and run a backtest

The `run_backtest.py` helper script downloads data using `yfinance` (or reads a
local CSV) and plots the results:

```bash
python -m src.run_backtest --symbol AAPL --start 2024-01-01 --end 2024-06-30 --output result.png
```

Use `--csv mydata.csv` to run on your own dataset without downloading.

### Run on the sample dataset

A small CSV file is provided under `data/sample.csv` for quick testing:

```bash
python -m src.backtest data/sample.csv --short 3 --long 5 --output sample.png
```

Both commands will generate a plot showing the closing price, moving averages
and the strategy equity curve.
