import bcrypt
import secrets

# ----------------------------
# Password hashing & checking
# ----------------------------
def hash_password(password: str) -> str:
    """
    Hash a plain-text password.
    """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash.
    """
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))

# ----------------------------
# Token generation
# ----------------------------
def generate_token(length: int = 32) -> str:
    """
    Generate a random secure token (for sessions or API keys).
    """
    return secrets.token_hex(length)
