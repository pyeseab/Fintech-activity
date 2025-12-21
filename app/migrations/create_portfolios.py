# app/migrations/create_portfolios.py
import sqlite3

conn = sqlite3.connect("portfolio.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS portfolios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sharpe_ratio REAL
)
""")

conn.commit()
conn.close()
