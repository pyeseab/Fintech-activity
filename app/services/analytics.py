import pandas as pd
import numpy as np

def calculate_performance(portfolio_df, price_col="price", risk_free_rate=0.0):
    # Check input
    if price_col not in portfolio_df.columns:
        raise ValueError(f"Portfolio DataFrame must contain '{price_col}' column.")

    # Daily returns (does not modify original df)
    returns = portfolio_df[price_col].pct_change().dropna()

    if len(returns) < 2:
        return {
            "cumulative_return": np.nan,
            "volatility": np.nan,
            "sharpe_ratio": np.nan
        }

    # Cumulative return
    cumulative_return = (1 + returns).prod() - 1

    # Annualized volatility
    volatility = returns.std(ddof=1) * np.sqrt(252)

    # Convert annual rf → daily
    daily_rf = (1 + risk_free_rate)**(1/252) - 1

    # Annualized excess return
    annual_excess_return = (returns.mean() - daily_rf) * 252

    sharpe_ratio = annual_excess_return / volatility if volatility > 0 else np.nan

    return {
        "cumulative_return": cumulative_return,
        "volatility": volatility,
        "sharpe_ratio": sharpe_ratio
    }
