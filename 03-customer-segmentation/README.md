# 👥 Customer Segmentation Using RFM & K-Means

## 📌 Project Overview

This project analyzes transactional data from an online retailer to identify meaningful customer segments based on purchasing behavior.

The analysis uses **RFM (Recency, Frequency, Monetary) analysis** combined with **K-Means clustering** to group customers according to how recently they purchased, how frequently they buy, and how much revenue they generate.

The objective is to transform raw transactional data into actionable customer insights that can support marketing, retention, and customer relationship strategies.

---

## 📊 Dataset

The dataset contains transactional records from a UK-based online retailer.

### Original Dataset

- **541,909 transactions**
- **8 variables**
- Transaction period: December 2010 – December 2011

Main variables include:

- Invoice number
- Product
- Quantity
- Transaction date
- Unit price
- Customer ID
- Country

After data cleaning:

- **397,884 valid transactions**
- **4,338 unique customers**
- **144,025 rows removed**
- **Total analyzed revenue: 8,911,407.90**

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- SQL
- Git / GitHub
- Visual Studio Code

---

## 🧹 Data Cleaning

Before customer segmentation, the dataset was cleaned to improve the reliability of the analysis.

The process included:

- Removing transactions without a valid Customer ID
- Removing missing product descriptions
- Removing invalid or cancelled transactions
- Removing transactions with non-positive quantities or prices
- Converting transaction dates to datetime format
- Creating total transaction value

---

## 📐 RFM Analysis

Customers were summarized using three behavioral metrics:

### Recency
Number of days since the customer's most recent purchase.

### Frequency
Number of unique transactions completed by the customer.

### Monetary
Total amount spent by the customer.

The transactional dataset was transformed into an RFM table containing **4,338 customer profiles**.

---

## 🤖 Machine Learning — K-Means Clustering

Before clustering, RFM variables were log-transformed to reduce the impact of highly skewed values and extreme customers.

The variables were then standardized using **StandardScaler**.

A **K-Means clustering model with 4 clusters** was used to identify distinct customer groups.

---

## 🎯 Customer Segments

| Segment | Customers | Avg. Recency | Avg. Frequency | Avg. Monetary |
|---|---:|---:|---:|---:|
| High-Value Customers | 716 | 12.13 | 13.71 | 8,074.27 |
| Recent Customers | 837 | 18.12 | 2.15 | 551.82 |
| Regular Customers | 1,173 | 71.08 | 4.08 | 1,802.83 |
| Inactive / At-Risk Customers | 1,612 | 182.50 | 1.32 | 343.45 |

---

## 💡 Key Insights

### ⭐ High-Value Customers

These customers represent the strongest customer group.

They purchase frequently, have purchased recently, and generate substantially higher average revenue.

**Business opportunity:** loyalty programs, personalized offers, VIP benefits, and retention strategies.

### 🆕 Recent Customers

These customers purchased recently but still have relatively low purchase frequency and monetary value.

**Business opportunity:** onboarding campaigns and targeted promotions to encourage repeat purchases.

### 🟢 Regular Customers

These customers show moderate purchasing frequency and spending but have been inactive longer than recent and high-value customers.

**Business opportunity:** personalized recommendations and re-engagement campaigns.

### ⚠️ Inactive / At-Risk Customers

This is the largest customer segment, with **1,612 customers**.

Their last purchase occurred approximately **183 days ago on average**, and they have the lowest purchasing frequency and monetary value.

**Business opportunity:** win-back campaigns, targeted discounts, and reactivation strategies.

---

## 📈 Visualizations

### Customers by Segment

![Customers by Segment](Images/Customers%20by%20Segment.png)

### Average Customer Value by Segment

![Average Customer Value by Segment](Images/Average%20Customer%20Value%20by%20Segment.png)

### Recency vs Frequency

![Recency vs Frequency](Images/Recency%20vs%20Frequency.png)

---

## 📁 Project Structure

```text
03-customer-segmentation/
│
├── Data/
│   ├── Online Retail.xlsx
│   └── customer_segments.csv
│
├── Images/
│   ├── Customers by Segment.png
│   ├── Average Customer Value by Segment.png
│   └── Recency vs Frequency.png
│
├── Python/
│   └── customer_segmentation.py
│
├── SQL/
│   ├── 01_create_table.sql
│   ├── 02_rfm_analysis.sql
│   └── 03_business_questions.sql
│
└── README.md
```

---

## 🚀 Business Value

This project demonstrates how transactional data can be transformed into customer intelligence using analytics and machine learning.

The resulting customer segments can support:

- Customer retention strategies
- Targeted marketing campaigns
- Loyalty programs
- Customer reactivation
- Personalized promotions
- Customer lifetime value initiatives

---

## 👨‍💻 Author

**Jose Gabriel Monsivais Hurtado**

Data Science Engineering Student  
Industrial Mechatronics Engineer