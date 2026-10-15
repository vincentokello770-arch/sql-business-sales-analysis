# Business Sales Analysis Report

## Executive Summary

This project analyzes 120 synthetic retail transactions using Python, SQLite, and SQL to evaluate sales performance across products, regions, months, and payment methods.

The dataset records **KES 7,060,800 in revenue across 120 transactions**, with an average transaction value of **KES 58,840**. Laptops contribute the largest share of revenue (59.84%), while card payments account for the highest revenue share among payment methods (28.55%).

These findings demonstrate how SQL can transform transaction-level data into business performance indicators. Because the dataset is synthetic, the results are illustrative rather than representative of actual market conditions.

All monetary values are expressed in Kenyan shillings (KES).

## 1. Project Overview

The objective is to demonstrate a reproducible analytics workflow: generate or load data, build a SQLite database, execute SQL queries, and communicate findings through a business report.

The analysis covers:
- Overall sales performance
- Product revenue and unit sales
- Regional performance
- Monthly revenue trends
- Average transaction value
- Payment-method performance
- Product revenue contribution

## 2. Key Performance Indicators

| Metric | Result |
|---|---:|
| Total transactions | 120 |
| Total units sold | 362 |
| Total revenue | KES 7,060,800 |
| Average transaction value | KES 58,840 |

Revenue is calculated as quantity multiplied by unit price. Average transaction value is calculated as total revenue divided by the number of transaction records.

## 3. Product Performance

| Product | Units Sold | Revenue (KES) | Revenue Share |
|---|---:|---:|---:|
| Laptop | 65 | 4,225,000 | 59.84% |
| Smartphone | 50 | 1,400,000 | 19.83% |
| Monitor | 59 | 1,062,000 | 15.04% |
| Headphones | 60 | 210,000 | 2.97% |
| Keyboard | 54 | 97,200 | 1.38% |
| Mouse | 74 | 66,600 | 0.94% |

### Findings

Laptops generated the highest revenue, contributing 59.84% of total sales revenue. Smartphones and monitors were the next-largest contributors.

Mice recorded the highest unit sales at 74 units but generated less revenue than any other product. This illustrates why unit volume and revenue contribution should be examined together.

### Recommendations

- Monitor laptop stock availability and sales demand.
- Review product-level costs and gross margins before making pricing or inventory decisions.
- Investigate whether high-volume, lower-revenue products support complementary sales or other business objectives.

## 4. Regional Performance

| Region | Transactions | Revenue (KES) |
|---|---:|---:|
| Mombasa | 23 | 1,801,000 |
| Kisumu | 20 | 1,443,500 |
| Nakuru | 30 | 1,416,700 |
| Nairobi | 29 | 1,390,100 |
| Eldoret | 18 | 1,009,500 |

### Findings

Mombasa generated the highest revenue, while Eldoret generated the lowest. Nakuru recorded the highest transaction count.

Revenue and transaction volume do not necessarily move together. Further analysis of average transaction value and product mix could help explain the regional differences.

### Recommendations

- Compare regional product mix and average transaction value.
- Investigate factors that may explain Mombasa's higher revenue.
- Use additional data before making regional inventory or marketing investment decisions.

## 5. Payment-Method Analysis

| Payment Method | Transactions | Revenue (KES) | Revenue Share |
|---|---:|---:|---:|
| Card | 39 | 2,015,900 | 28.55% |
| M-Pesa | 27 | 1,917,400 | 27.16% |
| Cash | 26 | 1,865,000 | 26.41% |
| Bank Transfer | 28 | 1,262,500 | 17.88% |

### Findings

Card payments generated the highest revenue share at 28.55%, followed by M-Pesa at 27.16%. Cash contributed 26.41%, while bank transfers contributed 17.88%.

The differences describe this dataset only. They do not establish customer payment preferences in the wider Kenyan market.

### Recommendations

- Compare payment methods by transaction value and transaction volume.
- Review payment processing costs and settlement requirements if real operational data becomes available.
- Consider customer convenience and transaction reliability before changing payment options.

## 6. Monthly Revenue Trends

| Month | Transactions | Units Sold | Revenue (KES) |
|---|---:|---:|---:|
| January 2026 | 11 | 28 | 468,300 |
| February 2026 | 16 | 49 | 1,062,900 |
| March 2026 | 13 | 42 | 719,600 |
| April 2026 | 17 | 55 | 961,100 |
| May 2026 | 16 | 45 | 1,660,800 |
| June 2026 | 15 | 40 | 500,700 |
| July 2026 | 6 | 17 | 93,800 |
| August 2026 | 17 | 54 | 937,500 |
| September 2026 | 9 | 32 | 656,100 |

### Findings

May recorded the highest monthly revenue at KES 1,660,800, while July recorded the lowest at KES 93,800.

Monthly revenue varies considerably across the dataset. Because the records are synthetic, these fluctuations should not be interpreted as evidence of seasonality or actual demand patterns.

## 7. Methodology

1. Generated a reproducible synthetic dataset using Python.
2. Loaded 120 transaction records from CSV into SQLite.
3. Created a sales table with data types and integrity constraints.
4. Used SQL aggregation, grouping, sorting, date functions, and scalar subqueries.
5. Analyzed revenue, product contribution, regional performance, monthly trends, and payment methods.
6. Verified the database record count and executed the analytical queries.

## 8. Tools and Skills Demonstrated

- **Python:** data generation and database automation
- **SQLite:** relational data storage and integrity constraints
- **SQL:** aggregation, grouping, sorting, date-based analysis, and subqueries
- **Data analytics:** KPI calculation, comparisons, and interpretation
- **Documentation:** reporting findings, recommendations, and limitations
- **Git and GitHub:** version control and project publication

## 9. Limitations

- The dataset is synthetic and does not represent actual business activity.
- Product costs, operating expenses, and profit margins are unavailable.
- Customer identifiers and customer-level purchasing behavior are not included.
- The dataset covers January to September 2026 and does not establish a full-year trend.
- Findings are descriptive and do not demonstrate causation.
- Revenue share indicates contribution to total revenue, not profitability.

## 10. Conclusion

This project demonstrates how Python, SQLite, and SQL can transform transaction records into structured business insights. It includes reproducible data preparation, database validation, seven analytical queries, and a documented interpretation of sales performance.

Future extensions could include profitability analysis, customer-level data, automated data-quality tests, and a Power BI dashboard.