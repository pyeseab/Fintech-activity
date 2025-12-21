import sqlite3
from typing import Generator

DB_PATH = "portfolio.db"

def get_db() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()
