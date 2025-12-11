from services.advice.engine import get_advice_for_portfolio
from connection import get_db

def advice_for_user_portfolios(user_id: int):
    db = next(get_db())
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name, sharpe_ratio FROM portfolios WHERE user_id = ?",
        (user_id,)
    )
    portfolios = cursor.fetchall()

    if not portfolios:
        return "No portfolios found for this user."

    advice_list = []
    for pid, name, sharpe in portfolios:
        advice_text = get_advice_for_portfolio(sharpe)
        advice_list.append(f"Portfolio '{name}': {advice_text}")

    return "\n".join(advice_list)
