import sqlite3

connection = sqlite3.connect("data/sales.db")

tables = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("=== DATABASE VERIFICATION ===")
print("Tables:", tables)

columns = connection.execute("PRAGMA table_info(sales)").fetchall()
print("\nSales table columns:")
for column in columns:
    print(f"- {column[1]}")

count = connection.execute("SELECT COUNT(*) FROM sales").fetchone()[0]
print(f"\nTransaction count: {count}")

connection.close()
