# Business Sales Analysis Report

## 1. Project Overview

This project analyzes 120 synthetic retail sales transactions using
Python and SQLite. The purpose is to demonstrate SQL querying,
data aggregation, and business performance analysis.

All monetary values are expressed in Kenyan shillings (KES).

## 2. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total transactions | 120 |
| Total units sold | 362 |
| Total sales revenue | KES 7,060,800 |

Revenue is calculated as quantity multiplied by unit price.

## 3. Product Performance

| Product | Units Sold | Revenue (KES) |
|---|---:|---:|
| Laptop | 65 | 4,225,000 |
| Smartphone | 50 | 1,400,000 |
| Monitor | 59 | 1,062,000 |
| Headphones | 60 | 210,000 |
| Keyboard | 54 | 97,200 |
| Mouse | 74 | 66,600 |

### Finding

Laptops generated the highest revenue at KES 4,225,000,
representing approximately 59.8% of total revenue.

Mice recorded the highest unit sales at 74 units but generated
KES 66,600 in revenue. Unit volume and revenue contribution
therefore provide different views of product performance.

### Recommendation

Monitor laptop demand and stock availability. Review the pricing,
costs, and margins of lower-revenue products before making
decisions about inventory or promotions.

## 4. Regional Performance

| Region | Transactions | Revenue (KES) |
|---|---:|---:|
| Mombasa | 23 | 1,801,000 |
| Kisumu | 20 | 1,443,500 |
| Nakuru | 30 | 1,416,700 |
| Nairobi | 29 | 1,390,100 |
| Eldoret | 18 | 1,009,500 |

### Finding

Mombasa generated the highest revenue, while Eldoret generated
the lowest revenue. Nakuru recorded the most transactions.

### Recommendation

Investigate what drives Mombasa's higher revenue. Compare
average transaction value, product mix, and customer demand
before allocating additional stock or marketing budgets.

## 5. Methodology

1. Generated a reproducible synthetic dataset with Python.
2. Imported 120 transactions into a SQLite database.
3. Defined a sales table with data types and validation constraints.
4. Used SQL aggregation, grouping, and sorting to analyze performance.
5. Executed queries and checked transaction counts and revenue.

## 6. Limitations

- The dataset is synthetic and does not represent actual business activity.
- Product costs, operating expenses, and profit margins are unavailable.
- Customer identifiers and customer-level behavior are not included.
- The dataset covers January to September 2026; it does not establish
  a full-year trend.
- Regional and product findings are descriptive, not causal.

## 7. Tools Used

- Python 3
- SQLite
- SQL
- PowerShell
- Git and GitHub

## 8. Conclusion

The analysis demonstrates how SQL can turn transaction records
into useful summaries of revenue, product performance, and
regional activity. The project can be extended with monthly
trend analysis, payment-method analysis, and profitability data.
