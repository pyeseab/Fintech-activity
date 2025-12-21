from fastapi import APIRouter
import bcrypt
from app.db.connection import get_db

# Create the router
router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
def add_user_endpoint(username: str, password: str, email: str | None = None):
    """
    Add a new user with a hashed password.
    """
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return {"error": f"Username '{username}' already exists."}

    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash.decode("utf-8"))
    )
    db.commit()

    return {"message": f"User '{username}' added successfully."}


@router.post("/verify")
def verify_user_endpoint(username: str, password: str):
    """
    Verify that the username/password combination is correct.
    """
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        return {"valid": False}

    password_hash = row[0].encode("utf-8")
    valid = bcrypt.checkpw(password.encode("utf-8"), password_hash)
    return {"valid": valid}
