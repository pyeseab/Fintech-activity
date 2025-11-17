import pandas as pd
import numpy as np

def calculate_performance(portfolio_df, price_col="price", risk_free_rate=0.0):
    """
    Calculate portfolio performance metrics.
    
    Parameters
    ----------
    portfolio_df : pd.DataFrame
        Must contain a column with asset or portfolio prices.
    price_col : str
        Name of the column containing the price data.
    risk_free_rate : float
        Annual risk-free rate for Sharpe ratio calculation.
        
    Returns
    -------
    dict
        Dictionary containing cumulative return, volatility, and Sharpe ratio.
    """

    # Validate required column
    if price_col not in portfolio_df.columns:
        raise ValueError(f"Portfolio DataFrame must contain '{price_col}' column.")

    # Calculate returns
    portfolio_df['returns'] = portfolio_df[price_col].pct_change()

    # Cumulative return (total growth of portfolio)
    cumulative_return = (1 + portfolio_df['returns'].dropna()).prod() - 1

    # Annualized volatility (assuming 252 trading days)
    volatility = portfolio_df['returns'].std() * np.sqrt(252)

    # Sharpe ratio
    # Annualized return = mean daily return * 252
    annual_return = portfolio_df['returns'].mean() * 252
    sharpe = (annual_return - risk_free_rate) / volatility if volatility != 0 else np.nan

    return {
        "cumulative_return": cumulative_return,
        "volatility": volatility,
        "sharpe_ratio": sharpe
    }
