from connection import get_db

def evaluate_sharpe(sharpe_ratio: float) -> str:
    """
    Return simple advice based on Sharpe Ratio.
    """
    if sharpe_ratio > 1.5:
        return "Excellent risk-adjusted returns! Portfolio looks strong."
    elif sharpe_ratio > 1.0:
        return "Good performance, but there may be room for improvement."
    elif sharpe_ratio > 0.5:
        return "Average performance, consider rebalancing or diversifying."
    else:
        return "Low risk-adjusted returns; portfolio may be underperforming."


def advice_for_user_portfolios(user_id: int):
    """
    Fetch all portfolios for a given user and return Sharpe ratio advice.
    """
    db = next(get_db())
    cursor = db.cursor()

    # Fetch portfolio id, name, and Sharpe ratio
    cursor.execute(
        "SELECT id, name, sharpe_ratio FROM portfolios WHERE user_id = ?",
        (user_id,)
    )
    portfolios = cursor.fetchall()

    if not portfolios:
        return "No portfolios found for this user."

    # Create advice for each portfolio
    advice_list = []
    for portfolio_id, name, sharpe in portfolios:
        advice_text = evaluate_sharpe(sharpe)
        advice_list.append(f"Portfolio '{name}': {advice_text}")

    # Combine all advice into a single string
    return "\n".join(advice_list)
