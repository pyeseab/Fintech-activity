from fastapi import APIRouter
from app.services.advice_engine import evaluate_sharpe
from app.db.connection import get_db

router = APIRouter(prefix="/portfolios")

@router.post("/")
def add_portfolio(user_id: int, name: str, sharpe_ratio: float):
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO portfolios (user_id, name, sharpe_ratio) VALUES (?, ?, ?)",
        (user_id, name, sharpe_ratio)
    )
    db.commit()

    return {"message": "Portfolio added"}

@router.get("/{user_id}")
def get_user_portfolios(user_id: int):
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute(
        "SELECT id, name, sharpe_ratio FROM portfolios WHERE user_id = ?",
        (user_id,)
    )

    return [
        {
            "id": pid,
            "name": name,
            "sharpe_ratio": sharpe,
            "advice": evaluate_sharpe(sharpe)
        }
        for pid, name, sharpe in cursor.fetchall()
    ]
