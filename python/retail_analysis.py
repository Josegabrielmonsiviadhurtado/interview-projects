import pandas as pd

df = pd.read_csv("../retail_sales_dataset.csv")

print("Ventas Totales:")
print(df["Total Amount"].sum())

print("\nVenta Promedio:")
print(df["Total Amount"].mean())

print("\nCategorías:")
print(df["Product Category"].value_counts())

print("\nTop Categorías por Ventas:")
print(df.groupby("Product Category")["Total Amount"].sum())