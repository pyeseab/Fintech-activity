import csv
from connection import get_db

def ingest_portfolio_from_csv(user_id: int, csv_file_path: str):
    """
    Ingests a portfolio CSV into the database.
    Validates data, normalizes weights, and stores rows in a single batch.
    """

    required_cols = {"ticker", "weight", "sharpe_ratio"}

    db = next(get_db())
    cursor = db.cursor()

    # Read and validate CSV
    rows = []
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        if not required_cols.issubset(reader.fieldnames):
            raise ValueError(
                f"CSV missing required columns: {required_cols - set(reader.fieldnames)}"
            )

        for line_num, row in enumerate(reader, start=2):
            ticker = (row.get("ticker") or "").strip().upper()
            if not ticker:
                raise ValueError(f"Missing ticker at line {line_num}")

            try:
                weight = float(row.get("weight", 0))
                sharpe = float(row.get("sharpe_ratio", 0))
            except ValueError:
                raise ValueError(f"Invalid numeric value at line {line_num}")

            if weight < 0:
                raise ValueError(f"Negative weight at line {line_num}")

            if sharpe < -5 or sharpe > 10:  # sanity check
                raise ValueError(f"Suspicious Sharpe ratio at line {line_num}")

            rows.append({"ticker": ticker, "weight": weight, "sharpe_ratio": sharpe})

    # Normalize weights
    total_weight = sum(r["weight"] for r in rows)
    if total_weight <= 0:
        raise ValueError("Total weight must be > 0")

    for r in rows:
        r["weight"] = r["weight"] / total_weight

    # Create portfolio batch (versioning)
    cursor.execute(
        "INSERT INTO portfolio_uploads (user_id) VALUES (?)",
        (user_id,)
    )
    upload_id = cursor.lastrowid

    # Bulk insert portfolio lines
    insert_payload = [
        (upload_id, r["ticker"], r["weight"], r["sharpe_ratio"])
        for r in rows
    ]

    cursor.executemany(
        """INSERT INTO portfolios 
           (upload_id, ticker, weight, sharpe_ratio)
           VALUES (?, ?, ?, ?)""",
        insert_payload
    )

    db.commit()
    return f"Portfolio uploaded successfully with ID {upload_id}."
