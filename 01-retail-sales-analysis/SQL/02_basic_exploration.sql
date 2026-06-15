SELECT *
FROM retail_sales
LIMIT 10;

SELECT COUNT(*) AS total_rows
FROM retail_sales;

SELECT DISTINCT product_category
FROM retail_sales;

SELECT 
    gender,
    COUNT(*) AS total_transactions
FROM retail_sales
GROUP BY gender;