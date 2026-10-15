# SQL Business Sales Analysis

A beginner-friendly, portfolio-ready data analytics project using
Python, SQLite, and SQL to analyze synthetic retail sales data.

## Project Objectives

- Build a relational database from a CSV dataset.
- Calculate sales revenue and units sold.
- Rank products by revenue.
- Compare regional sales performance.
- Analyze monthly revenue trends.
- Communicate findings through a business report.

## Technology Stack

- Python 3.10+
- SQLite
- SQL
- Git and GitHub

No third-party Python packages or database server are required.

## Dataset

The dataset contains 120 synthetic transactions from a fictional
Kenyan retail business. It includes order dates, regions, products,
quantities, unit prices, and payment methods.

All monetary values are expressed in Kenyan shillings (KES).
The data is fictional and is intended for educational purposes only.

## Project Structure

```text
sql-business-sales-analysis/
├── data/
│   └── sales_data.csv
├── reports/
│   └── business_insights.md
├── sql/
│   └── sales_analysis.sql
├── build_database.py
├── generate_data.py
├── run_analysis.py
├── verify_database.py
├── README.md
├── requirements.txt
└── .gitignore
```

The SQLite database is generated locally and is not committed
to the repository.

## How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd sql-business-sales-analysis
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### 2. Generate the dataset (optional)

The supplied CSV is already included. To regenerate the same
synthetic dataset, run:

```bash
python generate_data.py
```

Regenerating the data replaces the existing CSV.

### 3. Build the database

```bash
python build_database.py
```

This creates `data/sales.db` and loads the sales records.

### 4. Verify the database

```bash
python verify_database.py
```

### 5. Execute the SQL analyses

```bash
python run_analysis.py
```

The runner executes the SQL statements in `sql/sales_analysis.sql`
and prints the results in the terminal.

## Key Findings

Based on the generated dataset:

- Total revenue: KES 7,060,800.
- Transactions: 120.
- Units sold: 362.
- Highest-revenue product: Laptop, at KES 4,225,000.
- Highest-revenue region: Mombasa, at KES 1,801,000.
- Highest-revenue month: May 2026, at KES 1,660,800.
- Lowest-revenue month: July 2026, at KES 93,800.

These results describe synthetic data and do not represent actual
business performance.

## SQL Skills Demonstrated

- `SELECT` and column aliases
- `SUM()` and `COUNT()`
- `GROUP BY` and `ORDER BY`
- Date grouping with SQLite `strftime()`
- Database table creation and data integrity constraints
- Parameterized inserts through Python's SQLite interface

## Business Report

See [reports/business_insights.md](reports/business_insights.md)
for the product rankings, regional comparison, recommendations,
methodology, and limitations.

## Limitations

This project measures sales revenue, not profit. Product costs,
operating expenses, and customer-level data are not available.
The synthetic dataset is designed to demonstrate analytical
techniques rather than support real commercial decisions.

## Future Improvements

- Add profit and gross-margin analysis.
- Analyze payment methods.
- Add automated data-quality tests.
- Build a dashboard using Power BI.
- Expand the dataset and compare performance across periods.

## Author

Created as a hands-on SQL and data analytics portfolio project.
