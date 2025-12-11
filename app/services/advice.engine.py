def evaluate_sharpe(sharpe_ratio: float) -> str:
    """
    Core logic for evaluating Sharpe ratio.
    Returns a simple advice string.
    """
    if sharpe_ratio > 1.5:
        return "Excellent risk-adjusted returns! Portfolio looks strong."
    elif sharpe_ratio > 1.0:
        return "Good performance, but there may be room for improvement."
    elif sharpe_ratio > 0.5:
        return "Average performance, consider rebalancing or diversifying."
    else:
        return "Low risk-adjusted returns; portfolio may be underperforming."


def get_advice_for_portfolio(sharpe_ratio: float) -> str:
    """
    Wrapper function that could later combine multiple metrics.
    Currently only uses Sharpe ratio.
    """
    return evaluate_sharpe(sharpe_ratio)
