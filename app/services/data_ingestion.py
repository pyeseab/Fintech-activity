#engine user provides user portfolio CSV optional match with yahoo database
import csv
from connection import get_db

def ingest_portfolio_from_csv(user_id: int, csv_file_path: str):
    """
    Load a portfolio from a CSV file and insert into the database.
    CSV expected format:
    ticker,weight,sharpe_ratio
    AAPL,0.5,1.2
    MSFT,0.5,1.1
    """
    db = next(get_db())
    cursor = db.cursor()

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row.get("ticker")
            weight = float(row.get("weight", 0))
            sharpe_ratio = float(row.get("sharpe_ratio", 0))

            cursor.execute(
                "INSERT INTO portfolios (user_id, name, sharpe_ratio) VALUES (?, ?, ?)",
                (user_id, name, sharpe_ratio)
            )
    db.commit()
    return f"Portfolio data from '{csv_file_path}' ingested successfully."
