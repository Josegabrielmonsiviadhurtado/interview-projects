-- ==========================================
-- BASIC EXPLORATION
-- ==========================================

-- Total employees
SELECT COUNT(*) AS total_employees
FROM employees;

-- Attrition distribution
SELECT
    Attrition,
    COUNT(*) AS employees
FROM employees
GROUP BY Attrition;

-- Overall attrition rate
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees;

-- Employees by department
SELECT
    Department,
    COUNT(*) AS employees
FROM employees
GROUP BY Department
ORDER BY employees DESC;

-- Average age
SELECT ROUND(AVG(Age), 2) AS average_age
FROM employees;

-- Average monthly income
SELECT ROUND(AVG(MonthlyIncome), 2) AS average_monthly_income
FROM employees;