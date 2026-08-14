import pandas as pd

import matplotlib.pyplot as plt

# ==========================================
# HR ATTRITION ANALYSIS
# ==========================================

# Load dataset
file_path = "../Data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

df = pd.read_csv(file_path)

# Basic dataset information
print("HR ATTRITION DATASET")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nAttrition distribution:")
print(df["Attrition"].value_counts())

print("\nAttrition rate:")
attrition_rate = (df["Attrition"] == "Yes").mean() * 100
print(f"{attrition_rate:.2f}%")

# ==========================================
# ATTRITION ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("ATTRITION ANALYSIS")
print("=" * 50)

# Attrition by department
department_attrition = pd.crosstab(
    df["Department"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by department:")
print(department_attrition.round(2))

# Attrition by overtime
overtime_attrition = pd.crosstab(
    df["OverTime"],
    df["Attrition"],
    normalize="index"
) * 100

print("\nAttrition rate by overtime:")
print(overtime_attrition.round(2))

# Average monthly income
income_attrition = df.groupby("Attrition")["MonthlyIncome"].mean()

print("\nAverage monthly income by attrition:")
print(income_attrition.round(2))

# Average age
age_attrition = df.groupby("Attrition")["Age"].mean()

print("\nAverage age by attrition:")
print(age_attrition.round(2))

# Average years at company
years_attrition = df.groupby("Attrition")["YearsAtCompany"].mean()

print("\nAverage years at company by attrition:")
print(years_attrition.round(2))

# ==========================================
# DATA VISUALIZATION
# ==========================================

# 1. Attrition distribution
attrition_counts = df["Attrition"].value_counts()

plt.figure(figsize=(7, 5))
attrition_counts.plot(kind="bar")
plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../images/Attrition Distribution.png")
plt.close()


# 2. Attrition rate by department
department_rate = (
    df.groupby("Department")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values()
)

plt.figure(figsize=(8, 5))
department_rate.plot(kind="bar")
plt.title("Attrition Rate by Department")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("../images/Attrition Rate by Department.png")
plt.close()


# 3. Attrition rate by overtime
overtime_rate = (
    df.groupby("OverTime")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

plt.figure(figsize=(7, 5))
overtime_rate.plot(kind="bar")
plt.title("Attrition Rate by Overtime")
plt.xlabel("Overtime")
plt.ylabel("Attrition Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../images/Attrition Rate by Overtime.png")
plt.close()


# 4. Average monthly income by attrition
average_income = df.groupby("Attrition")["MonthlyIncome"].mean()

plt.figure(figsize=(7, 5))
average_income.plot(kind="bar")
plt.title("Average Monthly Income by Attrition")
plt.xlabel("Attrition")
plt.ylabel("Average Monthly Income")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("../images/Average Monthly Income by Attrition.png")
plt.close()

print("\nCharts saved successfully in the images folder.")