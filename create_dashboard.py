import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Project paths
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "data" / "sales_data.csv"
OUTPUT_DIR = BASE_DIR / "reports"
OUTPUT_FILE = OUTPUT_DIR / "sales_dashboard.png"

# Load sales data
with CSV_FILE.open("r", newline="", encoding="utf-8-sig") as file:
    rows = list(csv.DictReader(file))

if not rows:
    raise ValueError("The sales CSV file contains no records.")

# Calculate metrics
total_revenue = 0
total_units = 0
product_revenue = defaultdict(float)
region_revenue = defaultdict(float)
monthly_revenue = defaultdict(float)
payment_revenue = defaultdict(float)

for row in rows:
    quantity = int(row["quantity"])
    price = float(row["unit_price"])
    revenue = quantity * price

    total_revenue += revenue
    total_units += quantity

    product_revenue[row["product_name"]] += revenue
    region_revenue[row["region"]] += revenue
    monthly_revenue[row["order_date"][:7]] += revenue
    payment_revenue[row["payment_method"]] += revenue

transaction_count = len(rows)
average_transaction = total_revenue / transaction_count

# Dashboard styling
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
})

fig = plt.figure(figsize=(16, 10), facecolor="#F4F6F9")
fig.suptitle(
    "KENYAN RETAIL SALES PERFORMANCE",
    fontsize=22,
    fontweight="bold",
    color="#183153",
    y=0.97,
)
fig.text(
    0.5, 0.935,
    "Business intelligence dashboard | January–September 2026",
    ha="center", fontsize=11, color="#586579",
)

# KPI cards
kpis = [
    ("TOTAL REVENUE", f"KES {total_revenue:,.0f}"),
    ("TRANSACTIONS", f"{transaction_count:,}"),
    ("UNITS SOLD", f"{total_units:,}"),
    ("AVG. TRANSACTION", f"KES {average_transaction:,.0f}"),
]

card_positions = [0.06, 0.29, 0.52, 0.75]
for x, (label, value) in zip(card_positions, kpis):
    ax = fig.add_axes([x, 0.79, 0.19, 0.095])
    ax.set_facecolor("white")
    for spine in ax.spines.values():
        spine.set_color("#DDE3EA")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(
        0.5, 0.68, label, ha="center", va="center",
        fontsize=9, color="#586579", fontweight="bold",
    )
    ax.text(
        0.5, 0.30, value, ha="center", va="center",
        fontsize=15, color="#183153", fontweight="bold",
    )

# Chart layout
ax_product = fig.add_axes([0.07, 0.45, 0.40, 0.27])
ax_region = fig.add_axes([0.55, 0.45, 0.38, 0.27])
ax_month = fig.add_axes([0.07, 0.10, 0.55, 0.27])
ax_payment = fig.add_axes([0.69, 0.10, 0.24, 0.27])

for ax in [ax_product, ax_region, ax_month, ax_payment]:
    ax.set_facecolor("white")
    ax.grid(axis="y", alpha=0.22)
    ax.set_axisbelow(True)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#DDE3EA")

# Revenue by product
products = sorted(product_revenue.items(), key=lambda item: item[1])
ax_product.barh(
    [item[0] for item in products],
    [item[1] for item in products],
    color="#2878B5",
)
ax_product.set_title("Revenue by Product", loc="left", pad=10)
ax_product.xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f"{x / 1_000_000:.1f}M")
)
ax_product.set_xlabel("Revenue (KES)")

# Revenue by region
regions = sorted(region_revenue.items(), key=lambda item: item[1], reverse=True)
ax_region.bar(
    [item[0] for item in regions],
    [item[1] for item in regions],
    color="#2A9D8F",
)
ax_region.set_title("Revenue by Region", loc="left", pad=10)
ax_region.yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda y, _: f"{y / 1_000_000:.1f}M")
)
ax_region.tick_params(axis="x", rotation=25)
ax_region.set_ylabel("Revenue (KES)")

# Monthly revenue trend
months = sorted(monthly_revenue.items())
ax_month.plot(
    [item[0] for item in months],
    [item[1] for item in months],
    color="#E76F51",
    marker="o",
    linewidth=2.5,
    markersize=6,
)
ax_month.fill_between(
    [item[0] for item in months],
    [item[1] for item in months],
    color="#E76F51",
    alpha=0.12,
)
ax_month.set_title("Monthly Revenue Trend", loc="left", pad=10)
ax_month.yaxis.set_major_formatter(
    mtick.FuncFormatter(lambda y, _: f"{y / 1_000_000:.1f}M")
)
ax_month.tick_params(axis="x", rotation=30)
ax_month.set_ylabel("Revenue (KES)")

# Revenue by payment method
payments = sorted(payment_revenue.items(), key=lambda item: item[1])
ax_payment.barh(
    [item[0] for item in payments],
    [item[1] for item in payments],
    color="#7A6FAC",
)
ax_payment.set_title("Revenue by Payment Method", loc="left", pad=10)
ax_payment.xaxis.set_major_formatter(
    mtick.FuncFormatter(lambda x, _: f"{x / 1_000_000:.1f}M")
)
ax_payment.set_xlabel("Revenue (KES)")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
fig.savefig(OUTPUT_FILE, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close(fig)

print("Dashboard created successfully.")
print(f"Transactions: {transaction_count:,}")
print(f"Total revenue: KES {total_revenue:,.2f}")
print(f"Units sold: {total_units:,}")
print(f"Saved to: {OUTPUT_FILE}")