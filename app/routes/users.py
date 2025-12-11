from connection import get_db

def add_user(username: str, email: str = None):
    """
    Add a new user to the database.
    """
    db = next(get_db())
    cursor = db.cursor()

    # Check if username already exists
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        return f"Username '{username}' already exists."

    # Insert new user
    cursor.execute(
        "INSERT INTO users (username, email) VALUES (?, ?)",
        (username, email)
    )
    db.commit()
    return f"User '{username}' added successfully."


def get_user_by_id(user_id: int):
    """
    Fetch user information by user ID.
    """
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute("SELECT id, username, email, created_at FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        uid, username, email, created_at = row
        return {
            "id": uid,
            "username": username,
            "email": email,
            "created_at": created_at
        }
    return None


def get_user_by_username(username: str):
    """
    Fetch user information by username.
    """
    db = next(get_db())
    cursor = db.cursor()

    cursor.execute("SELECT id, username, email, created_at FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row:
        uid, uname, email, created_at = row
        return {
            "id": uid,
            "username": uname,
            "email": email,
            "created_at": created_at
        }
    return None
