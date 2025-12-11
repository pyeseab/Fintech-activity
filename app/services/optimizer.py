#User uploads portfolio (via data.ingestion.py)

#You fetch historical returns for the assets

#Call optimizer.optimize_portfolio()

#Return recommended weights + expected Sharpe ratio

#Advice engine can then comment on the new portfolio

import numpy as np

def optimize_portfolio(returns: np.ndarray, risk_free_rate: float = 0.0):
    """
    Simplified mean-variance optimizer to maximize Sharpe ratio.
    
    :param returns: 2D array (n_days x n_assets) of historical returns
    :param risk_free_rate: risk-free rate for Sharpe ratio calculation
    :return: dictionary of optimal weights per asset
    """
    n_assets = returns.shape[1]
    mean_returns = np.mean(returns, axis=0)
    cov_matrix = np.cov(returns.T)

    # Start with equal weights
    weights = np.ones(n_assets) / n_assets

    # Simplified: calculate Sharpe ratio for this allocation
    portfolio_return = np.dot(weights, mean_returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_volatility

    # Normally, you would use scipy.optimize.minimize here to maximize Sharpe
    # This is a placeholder for now
    return {
        "weights": weights.tolist(),
        "expected_return": portfolio_return,
        "volatility": portfolio_volatility,
        "sharpe_ratio": sharpe_ratio
    }
