-- Business Question 1:
-- What is the total sales revenue?

SELECT
    COUNT(*) AS total_transactions,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue_kes
FROM sales;

-- Business Question 2:
-- Which products generate the most revenue?

SELECT
    product_name,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS revenue_kes
FROM sales
GROUP BY product_name
ORDER BY revenue_kes DESC;

-- Business Question 3:
-- Which regions generate the most revenue?

SELECT
    region,
    COUNT(*) AS total_transactions,
    ROUND(SUM(quantity * unit_price), 2) AS revenue_kes
FROM sales
GROUP BY region
ORDER BY revenue_kes DESC;

-- Business Question 4:
-- How does sales revenue change month by month?

SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS revenue_kes
FROM sales
GROUP BY strftime('%Y-%m', order_date)
ORDER BY sales_month;
-- Business Question 5:
-- What is the average revenue per transaction?

SELECT
    COUNT(*) AS total_transactions,
    ROUND(SUM(quantity * unit_price), 2) AS total_revenue_kes,
    ROUND(AVG(quantity * unit_price), 2) AS average_transaction_value_kes
FROM sales;

-- Business Question 6:
-- How do payment methods compare in transaction volume and revenue?

SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS units_sold,
    ROUND(SUM(quantity * unit_price), 2) AS revenue_kes,
    ROUND(
        100.0 * SUM(quantity * unit_price) /
        (SELECT SUM(quantity * unit_price) FROM sales),
        2
    ) AS revenue_share_percent
FROM sales
GROUP BY payment_method
ORDER BY revenue_kes DESC;

-- Business Question 7:
-- What percentage of total revenue comes from each product?

SELECT
    product_name,
    ROUND(SUM(quantity * unit_price), 2) AS revenue_kes,
    ROUND(
        100.0 * SUM(quantity * unit_price) /
        (SELECT SUM(quantity * unit_price) FROM sales),
        2
    ) AS revenue_share_percent
FROM sales
GROUP BY product_name
ORDER BY revenue_kes DESC;
