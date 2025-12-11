# for migrations in django or sql academy or prisma i am told. helps move database to models created with changes updated
#the following code is for connection.py file to create portfolios for users
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
