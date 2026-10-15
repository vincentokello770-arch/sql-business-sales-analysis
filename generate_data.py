import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

products = [
    ("P001", "Laptop", 65000),
    ("P002", "Smartphone", 28000),
    ("P003", "Keyboard", 1800),
    ("P004", "Mouse", 900),
    ("P005", "Monitor", 18000),
    ("P006", "Headphones", 3500),
]

regions = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret"]
payment_methods = ["M-Pesa", "Card", "Cash", "Bank Transfer"]

output_file = Path("data") / "sales_data.csv"
start_date = date(2026, 1, 1)

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "order_id", "order_date", "region", "product_id",
        "product_name", "quantity", "unit_price",
        "payment_method"
    ])

    for order_id in range(1, 121):
        product_id, product_name, unit_price = random.choice(products)
        order_date = start_date + timedelta(days=random.randint(0, 272))
        quantity = random.randint(1, 5)

        writer.writerow([
            order_id,
            order_date.isoformat(),
            random.choice(regions),
            product_id,
            product_name,
            quantity,
            unit_price,
            random.choice(payment_methods),
        ])

print(f"Dataset created: {output_file}")
print("Transactions generated: 120")
print(f"Products available: {len(products)}")
print(f"Regions available: {len(regions)}")
