import sqlite3
from pathlib import Path

database = Path("data/sales.db")
sql_file = Path("sql/sales_analysis.sql")

sql_text = sql_file.read_text(encoding="utf-8-sig")

statements = []
buffer = ""

for line in sql_text.splitlines():
    buffer += line + "\n"
    if sqlite3.complete_statement(buffer):
        statement = buffer.strip()
        buffer = ""

        # Remove leading SQL comment lines.
        lines = [
            item for item in statement.splitlines()
            if not item.strip().startswith("--")
        ]
        statement = "\n".join(lines).strip()

        if statement:
            statements.append(statement)

if buffer.strip():
    raise ValueError("The SQL file contains an incomplete statement.")

with sqlite3.connect(database) as connection:
    executed = 0

    for number, query in enumerate(statements, start=1):
        if not query.upper().startswith("SELECT"):
            continue

        cursor = connection.execute(query)
        headers = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        print(f"\n{'=' * 65}")
        print(f"QUERY {number}")
        print("=" * 65)
        print(" | ".join(headers))

        for row in rows:
            print(" | ".join(str(value) for value in row))

        print(f"Rows returned: {len(rows)}")
        executed += 1

    print(f"\nSQL analysis completed. Queries executed: {executed}")
