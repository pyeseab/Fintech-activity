import bcrypt
from connection import get_db

def add_user(username: str, password: str, email: str = None):
    """
    Add a new user with a hashed password.
    """
    db = next(get_db())
    cursor = db.cursor()

    # Check if username already exists
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return f"Username '{username}' already exists."

    # Hash the password
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Insert new user
    cursor.execute(
        "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
        (username, email, password_hash.decode("utf-8"))
    )
    db.commit()
    return f"User '{username}' added successfully."


def verify_user(username: str, password: str) -> bool:
    """
    Verify that the username/password combination is correct.
    """
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if not row:
        return False

    password_hash = row[0].encode("utf-8")
    return bcrypt.checkpw(password.encode("utf-8"), password_hash)
