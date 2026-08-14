# HR Attrition Analysis

## Project Overview
Analyze employee attrition data to identify factors that influence employee turnover.

## Tools Used
- Python
- SQL
- Power BI
- Tableau

## Project Status
📋 Planned



# HR Attrition Analysis

## 📌 Project Overview

Employee attrition can have a significant impact on organizational performance, productivity, and recruitment costs.

This project analyzes the **IBM HR Analytics Employee Attrition & Performance dataset** to identify patterns associated with employee turnover and provide data-driven insights that could support employee retention strategies.

The analysis was performed using **Python and SQL**, with visualizations created to communicate the main findings.

---

## 🎯 Business Questions

This project focuses on answering the following questions:

1. What is the overall employee attrition rate?
2. Which departments have the highest attrition rates?
3. Is overtime associated with higher employee attrition?
4. How does monthly income differ between employees who stay and employees who leave?
5. Are younger employees more likely to leave?
6. How does employee tenure differ between employees who stay and those who leave?

---

## 🛠️ Tools Used

* Python
* Pandas
* Matplotlib
* SQL
* VS Code
* Git & GitHub

---

## 📊 Dataset

The dataset contains:

* **1,470 employees**
* **35 variables**
* **0 missing values**

Variables include employee demographics, job characteristics, compensation, overtime, satisfaction indicators, job roles, and years of experience.

---

## 🔎 Key Findings

### Overall Attrition

The overall employee attrition rate is:

**16.12%**

Out of 1,470 employees:

* 1,233 remained with the company.
* 237 left the company.

### Overtime

Overtime showed one of the strongest associations with employee attrition.

* Employees without overtime: **10.44% attrition**
* Employees with overtime: **30.53% attrition**

Employees working overtime had an attrition rate almost three times higher than employees who did not work overtime.

### Department

Attrition rates by department:

* Sales: **20.63%**
* Human Resources: **19.05%**
* Research & Development: **13.84%**

Sales had the highest attrition rate among the analyzed departments.

### Monthly Income

Average monthly income:

* Employees who stayed: **6,832.74**
* Employees who left: **4,787.09**

Employees who left had substantially lower average monthly income.

### Age

Average employee age:

* Employees who stayed: **37.56 years**
* Employees who left: **33.61 years**

Employees who left were younger on average.

### Years at Company

Average tenure:

* Employees who stayed: **7.37 years**
* Employees who left: **5.13 years**

Employees who left had shorter average tenure.

---

## 📈 Visualizations

The Python analysis generates visualizations for:

* Employee Attrition Distribution
* Attrition Rate by Department
* Attrition Rate by Overtime
* Average Monthly Income by Attrition

The generated charts are stored in the `images` directory.

---

## 💡 Business Insights

The analysis suggests that overtime, compensation, age, department, and employee tenure are associated with differences in attrition.

Overtime represents a particularly important signal because employees working overtime showed a considerably higher attrition rate.

Organizations could use these findings as a starting point to investigate workload, compensation, career development, and retention strategies, particularly among employees with high overtime and shorter tenure.

These results represent **associations within the dataset and should not be interpreted as proof of causation**.

---

## 📂 Project Structure

```text
02-hr-attrition-analysis/
│
├── Data/
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── images/
│   ├── Attrition Distribution.png
│   ├── Attrition Rate by Department.png
│   ├── Attrition Rate by Overtime.png
│   └── Average Monthly Income by Attrition.png
│
├── python/
│   └── HR_attrition_analysis.py
│
├── SQL/
│   ├── 01_create_table.sql
│   ├── 02_basic_exploration.sql
│   └── 03_business_questions.sql
│
└── README.md
```

## 🚀 Skills Demonstrated

* Exploratory Data Analysis (EDA)
* Data manipulation with Pandas
* Business-oriented data analysis
* SQL querying
* KPI calculation
* Data visualization
* Employee attrition analysis
* Translating data into actionable business insights

## 👤 Author

**Jose Gabriel Monsivais Hurtado**

Data Science Engineering Student
Interested in Data Analytics, Data Science and Data Engineering
