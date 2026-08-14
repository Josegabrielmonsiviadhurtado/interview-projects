-- ==========================================
-- HR ATTRITION ANALYSIS
-- Create Employee Table
-- ==========================================

CREATE TABLE employees (
    Age INTEGER,
    Attrition VARCHAR(10),
    BusinessTravel VARCHAR(50),
    DailyRate INTEGER,
    Department VARCHAR(50),
    DistanceFromHome INTEGER,
    Education INTEGER,
    EducationField VARCHAR(50),
    EmployeeCount INTEGER,
    EmployeeNumber INTEGER PRIMARY KEY,
    EnvironmentSatisfaction INTEGER,
    Gender VARCHAR(20),
    HourlyRate INTEGER,
    JobInvolvement INTEGER,
    JobLevel INTEGER,
    JobRole VARCHAR(100),
    JobSatisfaction INTEGER,
    MaritalStatus VARCHAR(20),
    MonthlyIncome INTEGER,
    MonthlyRate INTEGER,
    NumCompaniesWorked INTEGER,
    Over18 VARCHAR(5),
    OverTime VARCHAR(5),
    PercentSalaryHike INTEGER,
    PerformanceRating INTEGER,
    RelationshipSatisfaction INTEGER,
    StandardHours INTEGER,
    StockOptionLevel INTEGER,
    TotalWorkingYears INTEGER,
    TrainingTimesLastYear INTEGER,
    WorkLifeBalance INTEGER,
    YearsAtCompany INTEGER,
    YearsInCurrentRole INTEGER,
    YearsSinceLastPromotion INTEGER,
    YearsWithCurrManager INTEGER
);