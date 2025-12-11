from routes.portfolio import get_user_portfolios
from services.advice.engine import get_advice_for_portfolio

def generate_user_report(user_id: int):
    """
    Generate a text report for all portfolios of a user.
    """
    portfolios = get_user_portfolios(user_id)
    if not portfolios:
        return "No portfolios found for this user."

    report_lines = []
    report_lines.append(f"Portfolio Report for User ID {user_id}")
    report_lines.append("="*40)

    for p in portfolios:
        name = p["name"]
        sharpe = p["sharpe_ratio"]
        advice = get_advice_for_portfolio(sharpe)
        report_lines.append(f"Portfolio: {name}")
        report_lines.append(f"Sharpe Ratio: {sharpe:.2f}")
        report_lines.append(f"Advice: {advice}")
        report_lines.append("-"*40)

    return "\n".join(report_lines)
