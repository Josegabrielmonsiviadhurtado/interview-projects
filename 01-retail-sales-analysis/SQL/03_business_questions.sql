-- 1. Total sales by product category
SELECT 
    product_category,
    SUM(total_amount) AS total_sales
FROM retail_sales
GROUP BY product_category
ORDER BY total_sales DESC;

-- 2. Total units sold by category
SELECT 
    product_category,
    SUM(quantity) AS total_units_sold
FROM retail_sales
GROUP BY product_category
ORDER BY total_units_sold DESC;

-- 3. Monthly sales trend
SELECT 
    DATE_TRUNC('month', transaction_date) AS sales_month,
    SUM(total_amount) AS total_sales
FROM retail_sales
GROUP BY sales_month
ORDER BY sales_month;

-- 4. Sales by gender
SELECT 
    gender,
    SUM(total_amount) AS total_sales
FROM retail_sales
GROUP BY gender
ORDER BY total_sales DESC;

-- 5. Average sales by age group
SELECT
    CASE
        WHEN age < 25 THEN 'Under 25'
        WHEN age BETWEEN 25 AND 34 THEN '25-34'
        WHEN age BETWEEN 35 AND 44 THEN '35-44'
        WHEN age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    SUM(total_amount) AS total_sales
FROM retail_sales
GROUP BY age_group
ORDER BY total_sales DESC;