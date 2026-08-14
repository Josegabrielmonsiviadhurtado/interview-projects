-- ==========================================
-- BUSINESS QUESTIONS
-- HR Attrition Analysis
-- ==========================================

-- 1. Which departments have the highest attrition rate?
SELECT
    Department,
    ROUND(
        100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY Department
ORDER BY attrition_rate DESC;


-- 2. Is overtime associated with higher attrition?
SELECT
    OverTime,
    COUNT(*) AS employees,
    SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) AS employees_left,
    ROUND(
        100.0 * SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS attrition_rate
FROM employees
GROUP BY OverTime
ORDER BY attrition_rate DESC;


-- 3. How does monthly income differ by attrition?
SELECT
    Attrition,
    ROUND(AVG(MonthlyIncome), 2) AS average_monthly_income
FROM employees
GROUP BY Attrition;


-- 4. How does age differ by attrition?
SELECT
    Attrition,
    ROUND(AVG(Age), 2) AS average_age
FROM employees
GROUP BY Attrition;


-- 5. How does tenure differ by attrition?
SELECT
    Attrition,
    ROUND(AVG(YearsAtCompany), 2) AS average_years_at_company
FROM employees
GROUP BY Attrition;