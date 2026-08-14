import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
# ==========================================
# CUSTOMER SEGMENTATION ANALYSIS
# ==========================================

# Load dataset
file_path = "../Data/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("ONLINE RETAIL DATASET")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)

# ==========================================
# DATA CLEANING
# ==========================================

print("\n" + "=" * 50)
print("DATA CLEANING")
print("=" * 50)

# Create a copy of the original dataset
clean_df = df.copy()

# Remove transactions without CustomerID
clean_df = clean_df.dropna(subset=["CustomerID"])

# Remove cancelled invoices
clean_df = clean_df[
    ~clean_df["InvoiceNo"].astype(str).str.startswith("C")
]

# Keep only positive quantities
clean_df = clean_df[clean_df["Quantity"] > 0]

# Keep only positive prices
clean_df = clean_df[clean_df["UnitPrice"] > 0]

# Convert CustomerID to integer
clean_df["CustomerID"] = clean_df["CustomerID"].astype(int)

# Create total transaction value
clean_df["TotalPrice"] = (
    clean_df["Quantity"] * clean_df["UnitPrice"]
)

print(f"Original rows: {len(df)}")
print(f"Clean rows: {len(clean_df)}")
print(f"Rows removed: {len(df) - len(clean_df)}")

print(f"\nUnique customers: {clean_df['CustomerID'].nunique()}")

print("\nDate range:")
print(f"From: {clean_df['InvoiceDate'].min()}")
print(f"To:   {clean_df['InvoiceDate'].max()}")

print("\nTotal revenue:")
print(f"{clean_df['TotalPrice'].sum():,.2f}")


# ==========================================
# RFM ANALYSIS
# ==========================================

print("\n" + "=" * 50)
print("RFM ANALYSIS")
print("=" * 50)

# Reference date: one day after the last transaction
reference_date = clean_df["InvoiceDate"].max() + pd.Timedelta(days=1)

# Create RFM table
rfm = clean_df.groupby("CustomerID").agg(
    Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
    Frequency=("InvoiceNo", "nunique"),
    Monetary=("TotalPrice", "sum")
).reset_index()

print(f"\nCustomers in RFM table: {len(rfm)}")

print("\nFirst 10 customers:")
print(rfm.head(10))

print("\nRFM statistics:")
print(rfm[["Recency", "Frequency", "Monetary"]].describe().round(2))

# ==========================================
# CUSTOMER SEGMENTATION WITH K-MEANS
# ==========================================

print("\n" + "=" * 50)
print("K-MEANS CUSTOMER SEGMENTATION")
print("=" * 50)

# Select RFM variables
rfm_features = rfm[["Recency", "Frequency", "Monetary"]].copy()

# RFM variables are highly skewed.
# Log transformation reduces the effect of extreme values.
rfm_log = np.log1p(rfm_features)

# Standardize variables
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)

# Create 4 customer clusters
kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

rfm["Cluster"] = kmeans.fit_predict(rfm_scaled)

print("\nCustomers per cluster:")
print(rfm["Cluster"].value_counts().sort_index())

# Cluster profiles
cluster_profile = rfm.groupby("Cluster").agg(
    Customers=("CustomerID", "count"),
    AvgRecency=("Recency", "mean"),
    AvgFrequency=("Frequency", "mean"),
    AvgMonetary=("Monetary", "mean")
).round(2)

print("\nCluster profiles:")
print(cluster_profile)

# ==========================================
# BUSINESS SEGMENT LABELS
# ==========================================

segment_names = {
    0: "Recent Customers",
    1: "High-Value Customers",
    2: "Regular Customers",
    3: "Inactive / At-Risk Customers"
}

rfm["Segment"] = rfm["Cluster"].map(segment_names)

print("\n" + "=" * 50)
print("CUSTOMER SEGMENTS")
print("=" * 50)

print("\nCustomers per segment:")
print(rfm["Segment"].value_counts())

segment_profile = rfm.groupby("Segment").agg(
    Customers=("CustomerID", "count"),
    AvgRecency=("Recency", "mean"),
    AvgFrequency=("Frequency", "mean"),
    AvgMonetary=("Monetary", "mean")
).round(2)

print("\nSegment profiles:")
print(segment_profile)

# ==========================================
# EXPORT RESULTS
# ==========================================

rfm.to_csv(
    "../Data/customer_segments.csv",
    index=False
)

print("\nCustomer segmentation exported successfully!")

# ==========================================
# VISUALIZATIONS
# ==========================================

print("\n" + "=" * 50)
print("CREATING VISUALIZATIONS")
print("=" * 50)

# 1. Customers per segment
segment_counts = rfm["Segment"].value_counts()

plt.figure(figsize=(10, 6))
segment_counts.plot(kind="bar")

plt.title("Customers by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Number of Customers")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig("../Images/Customers by Segment.png", dpi=300)
plt.close()


# 2. Average monetary value by segment
monetary_segment = (
    rfm.groupby("Segment")["Monetary"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
monetary_segment.plot(kind="bar")

plt.title("Average Customer Value by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Average Monetary Value")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig("../Images/Average Customer Value by Segment.png", dpi=300)
plt.close()


# 3. Recency vs Frequency
plt.figure(figsize=(10, 6))

for segment in rfm["Segment"].unique():
    subset = rfm[rfm["Segment"] == segment]

    plt.scatter(
        subset["Recency"],
        subset["Frequency"],
        alpha=0.5,
        label=segment
    )

plt.title("Customer Segmentation: Recency vs Frequency")
plt.xlabel("Recency (Days)")
plt.ylabel("Frequency")
plt.legend()
plt.tight_layout()

plt.savefig("../Images/Recency vs Frequency.png", dpi=300)
plt.close()

print("\n3 visualizations created successfully!")