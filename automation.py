import pandas as pd

# Load data
df = pd.read_csv("data/Sample-Superstore.csv", encoding="latin1")

# Remove duplicate
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

# Save cleaned file
df.to_csv("output/cleaned_data.csv", index=False)

# Export KPI
kpi = pd.DataFrame({
    "Metric":["Total sales","Total Profit"],
    "Value":[total_sales, total_profit]
})

kpi. to_excel("output/KPI_Report.xlsx", index=False)

print("Done")