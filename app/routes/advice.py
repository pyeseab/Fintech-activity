from fastapi import APIRouter
from app.services.advice_engine import get_advice_for_portfolio
from app.db.connection import get_db

# Create the router
router = APIRouter(prefix="/advice", tags=["advice"])

@router.get("/user/{user_id}")
def advice_for_user(user_id: int):
    """
    Get advice for all portfolios of a given user.
    """
    db = next(get_db())
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name, sharpe_ratio FROM portfolios WHERE user_id = ?",
        (user_id,)
    )
    portfolios = cursor.fetchall()

    if not portfolios:
        return {"message": "No portfolios found for this user."}

    advice_list = []
    for pid, name, sharpe in portfolios:
        advice_text = get_advice_for_portfolio(sharpe)
        advice_list.append({"portfolio": name, "advice": advice_text})

    return {"advice": advice_list}
