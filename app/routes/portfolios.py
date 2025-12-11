from connection import get_db
from advice import evaluate_sharpe

def add_portfolio(user_id: int, name: str, sharpe_ratio: float):
    """
    Add a new portfolio for a user.
    """
    db = next(get_db())
    cursor = db.cursor()
    
    cursor.execute(
        "INSERT INTO portfolios (user_id, name, sharpe_ratio) VALUES (?, ?, ?)",
        (user_id, name, sharpe_ratio)
    )
    db.commit()
    return f"Portfolio '{name}' added successfully."


def get_user_portfolios(user_id: int):
    """
    Return all portfolios for a user.
    """
    db = next(get_db())
    cursor = db.cursor()
    
    cursor.execute(
        "SELECT id, name, sharpe_ratio FROM portfolios WHERE user_id = ?",
        (user_id,)
    )
    portfolios = cursor.fetchall()
    
    if not portfolios:
        return []
    
    # Return as list of dictionaries for easier usage
    return [
        {"id": pid, "name": name, "sharpe_ratio": sharpe, 
         "advice": evaluate_sharpe(sharpe)}
        for pid, name, sharpe in portfolios
    ]
