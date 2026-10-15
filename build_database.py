import csv
import sqlite3
from pathlib import Path

DATA_FILE = Path("data/sales_data.csv")
DB_FILE = Path("data/sales.db")

if not DATA_FILE.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_FILE}")

with sqlite3.connect(DB_FILE) as conn:
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS sales")

    cursor.execute("""
        CREATE TABLE sales (
            order_id INTEGER PRIMARY KEY,
            order_date TEXT NOT NULL,
            region TEXT NOT NULL,
            product_id TEXT NOT NULL,
            product_name TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            unit_price REAL NOT NULL CHECK (unit_price >= 0),
            payment_method TEXT NOT NULL
        )
    """)

    with DATA_FILE.open("r", newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        records = [
            (
                int(row["order_id"]),
                row["order_date"],
                row["region"],
                row["product_id"],
                row["product_name"],
                int(row["quantity"]),
                float(row["unit_price"]),
                row["payment_method"],
            )
            for row in reader
        ]

    cursor.executemany("""
        INSERT INTO sales (
            order_id, order_date, region, product_id,
            product_name, quantity, unit_price, payment_method
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, records)

    conn.commit()

    row_count = cursor.execute(
        "SELECT COUNT(*) FROM sales"
    ).fetchone()[0]

    total_revenue = cursor.execute("""
        SELECT ROUND(SUM(quantity * unit_price), 2)
        FROM sales
    """).fetchone()[0]

    invalid_rows = cursor.execute("""
        SELECT COUNT(*)
        FROM sales
        WHERE order_date IS NULL
           OR region IS NULL
           OR product_name IS NULL
           OR quantity <= 0
           OR unit_price < 0
    """).fetchone()[0]

    print("DATABASE BUILD SUCCESSFUL")
    print(f"Database: {DB_FILE}")
    print(f"Transactions loaded: {row_count}")
    print(f"Gross sales revenue: KES {total_revenue:,.2f}")
    print(f"Invalid rows detected: {invalid_rows}")
    print("Table: sales")
