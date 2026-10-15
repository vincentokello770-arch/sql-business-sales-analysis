# SQL Business Sales Analysis

A hands-on data analytics project using **Python, SQLite, and SQL** to analyze synthetic retail sales data for a fictional Kenyan business. The project demonstrates how raw transaction data can be transformed into a database, analyzed with SQL, and translated into actionable business insights.

## Project Objectives

- Build a relational database from a CSV dataset.
- Calculate total revenue, transactions, and units sold.
- Rank products by revenue.
- Compare regional sales performance.
- Analyze monthly revenue trends.
- Document findings and business recommendations.

## Technology Stack

- **Python 3.10+** — dataset generation, database creation, and query execution
- **SQLite** — relational database storage
- **SQL** — aggregation, grouping, ranking, and date-based analysis
- **Git and GitHub** — version control and project publishing

No third-party Python packages or separate database server are required.

## Dataset

The dataset contains **120 synthetic retail transactions** from a fictional Kenyan business. Fields include order dates, regions, product details, quantities, unit prices, and payment methods.

All monetary values are expressed in Kenyan shillings (KES). The data is fictional and intended for educational purposes.

## Key Results

| Metric | Result |
|---|---:|
| Total revenue | KES 7,060,800 |
| Transactions | 120 |
| Units sold | 362 |
| Highest-revenue product | Laptop |
| Laptop revenue | KES 4,225,000 |
| Highest-revenue region | Mombasa |
| Mombasa revenue | KES 1,801,000 |
| Highest-revenue month | May 2026 |
| May revenue | KES 1,660,800 |

These results describe the synthetic dataset, not actual commercial performance. Revenue is not profit.

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

The SQLite database is generated locally and excluded from version control. This keeps the repository lightweight and demonstrates a reproducible workflow.

## How to Run the Project

### Prerequisites

Install Python 3.10 or later and Git. Confirm they are available:

```powershell
python --version
git --version
```

### 1. Clone the repository

```powershell
git clone https://github.com/vincentokello770-arch/sql-business-sales-analysis.git
cd sql-business-sales-analysis
```

### 2. Generate the dataset (optional)

The supplied CSV is already included. To regenerate the synthetic dataset:

```powershell
python generate_data.py
```

This replaces the existing CSV with a reproducible dataset.

### 3. Build the SQLite database

```powershell
python build_database.py
```

This creates `data/sales.db` and loads the sales records.

### 4. Verify the database

```powershell
python verify_database.py
```

### 5. Run the SQL analyses

```powershell
python run_analysis.py
```

The runner executes the SQL statements in `sql/sales_analysis.sql` and prints the analysis results in the terminal.

## SQL Skills Demonstrated

- `SELECT` and column aliases
- Aggregate functions: `SUM()` and `COUNT()`
- `GROUP BY` and `ORDER BY`
- Monthly grouping with SQLite `strftime()`
- Table creation and data integrity constraints
- Parameterized SQL inserts using Python's `sqlite3` module
- Validation of loaded records and analytical results

## Business Report

Read the [Business Insights Report](reports/business_insights.md) for product rankings, regional comparisons, monthly performance, recommendations, methodology, and limitations.

## Limitations

This project analyzes sales revenue, not profit. Product costs, operating expenses, and customer-level data are unavailable. Because the dataset is synthetic, the findings should not be used to make real commercial decisions.

## Future Improvements

- Add product costs and gross-margin analysis.
- Analyze payment methods and transaction patterns.
- Implement automated data-quality tests.
- Build a Power BI dashboard.
- Expand the dataset to compare performance across longer periods.

## Author

**Vincent Kenyatta**  
ICT Professional | SQL & Data Analytics Practitioner | Technology Educator

[GitHub Profile](https://github.com/vincentokello770-arch) · [Project Repository](https://github.com/vincentokello770-arch/sql-business-sales-analysis)

This project was developed as a hands-on portfolio exercise to demonstrate practical SQL, Python, database, and business analytics skills.