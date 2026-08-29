
import pandas as pd
import matplotlib.pyplot as plt



print("Pandas successfully imported!")

df = pd.read_csv("data/superstore dataset.csv", encoding="latin1")

print(df.head())

print(df.columns)

(df.info())

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print(df[["Order Date", "Ship Date"]].dtypes)

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

print("Total Sales:", total_sales)

print("Total Profit:", total_profit)


# Monthly Sales Analysis

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print(monthly_sales)


# Monthly Sales Graph

plt.figure(figsize=(12, 6))

plt.plot(monthly_sales.index.astype(str), monthly_sales.values)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("charts/monthly_sales_trend.png")

plt.show()

# Year-wise Sales Analysis

df["Year"] = df["Order Date"].dt.year

yearly_sales = df.groupby("Year")["Sales"].sum()

print("Yearly Sales:")
print(yearly_sales)

# Year-wise Sales Graph

plt.figure(figsize=(8, 5))

plt.bar(yearly_sales.index.astype(str), yearly_sales.values)

plt.title("Yearly Sales")

plt.xlabel("Year")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("charts/yearly_sales.png")

plt.show()

# Category-wise Sales Analysis

category_sales = df.groupby("Category")["Sales"].sum()

print("Category-wise Sales:")
print(category_sales)


# Category-wise Sales Graph

plt.figure(figsize=(8, 5))

plt.bar(category_sales.index, category_sales.values)

plt.title("Sales by Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("charts/category_sales.png")

plt.show()

# Year-wise Profit Analysis

yearly_profit = df.groupby("Year")["Profit"].sum()

print("Yearly Profit:")
print(yearly_profit)

# Year-wise Profit Graph

plt.figure(figsize=(8, 5))

plt.bar(yearly_profit.index.astype(str), yearly_profit.values)

plt.title("Yearly Profit")

plt.xlabel("Year")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/yearly_profit.png")

plt.show()

# Category-wise Profit Analysis

category_profit = df.groupby("Category")["Profit"].sum()

print("Category-wise Profit:")
print(category_profit)


# Category-wise Profit Graph

plt.figure(figsize=(8, 5))

plt.bar(category_profit.index, category_profit.values)

plt.title("Profit by Category")

plt.xlabel("Category")

plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("charts/category_profit.png")

plt.show()

# Discount vs Profit Analysis

discount_profit = df.groupby("Discount")["Profit"].mean()

print("Average Profit by Discount:")
print(discount_profit)

# Discount vs  Profit Graph

plt.figure(figsize=(10, 6))

plt.plot(discount_profit.index, discount_profit.values, marker="o")

plt.title("Discount vs Average Profit")

plt.xlabel("Discount")

plt.ylabel("Average Profit")

plt.grid(True)

plt.savefig("charts/discount_vs_profit.png")

plt.show()

# Sub-Category Sales and Profit Analysis

subcategory_analysis = df.groupby("Sub-Category")[["Sales", "Profit"]].sum()

print("Sub-Category Sales and Profit:")
print(subcategory_analysis.sort_values("Profit"))

# Sub-Category Profit Graph

plt.figure(figsize=(10, 7))

plt.barh(subcategory_analysis.index, subcategory_analysis["Profit"])

plt.title("Profit by Sub-Category")

plt.xlabel("Total Profit")

plt.ylabel("Sub-Category")

plt.tight_layout()

plt.savefig("charts/subcategory_profit.png")

plt.show()

# Sub-Category Sales Graph

plt.figure(figsize=(10, 7))

plt.barh(subcategory_analysis.index, subcategory_analysis["Sales"])

plt.title("Sales by Sub-Category")

plt.xlabel("Total Sales")

plt.ylabel("Sub-Category")

plt.tight_layout()

plt.savefig("charts/subcategory_sales.png")

plt.show()

# Sub-Category Discount Analysis

subcategory_discount = df.groupby("Sub-Category")["Discount"].mean()

print("Average Discount by Sub-Category:")
print(subcategory_discount.sort_values(ascending=False))
# Sub-Category Discount Graph

plt.figure(figsize=(10, 7))

plt.barh(subcategory_discount.index, subcategory_discount.values)

plt.title("Average Discount by Sub-Category")

plt.xlabel("Average Discount")

plt.ylabel("Sub-Category")

plt.tight_layout()

plt.savefig("charts/subcategory_discount.png")

plt.show()

# Loss-Making Sub-Categories

loss_making = subcategory_analysis[subcategory_analysis["Profit"] < 0]

print("Loss-Making Sub-Categories:")
print(loss_making)

# Loss-Making Sub-Categories Graph

plt.figure(figsize=(8, 5))

plt.bar(loss_making.index, loss_making["Profit"])

plt.title("Loss-Making Sub-Categories")

plt.xlabel("Sub-Category")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/loss_making_subcategories.png")

plt.show()

# Top Profitable Sub-Categories

top_profit = subcategory_analysis.sort_values("Profit", ascending=False).head(5)

print("Top 5 Profitable Sub-Categories:")
print(top_profit)
# Top 5 Profitable Sub-Categories Graph

plt.figure(figsize=(8, 5))

plt.bar(top_profit.index, top_profit["Profit"])

plt.title("Top 5 Profitable Sub-Categories")

plt.xlabel("Sub-Category")

plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/top_5_profitable_subcategories.png")

plt.show()

# Profit Margin by Sub-Category

subcategory_analysis["Profit Margin"] = (
    subcategory_analysis["Profit"] / subcategory_analysis["Sales"]
) * 100

print("Profit Margin by Sub-Category:")
print(subcategory_analysis[["Sales", "Profit", "Profit Margin"]].sort_values("Profit Margin"))

# Profit Margin Graph

plt.figure(figsize=(10, 7))

plt.barh(subcategory_analysis.index, subcategory_analysis["Profit Margin"])

plt.title("Profit Margin by Sub-Category")

plt.xlabel("Profit Margin (%)")

plt.ylabel("Sub-Category")

plt.tight_layout()

plt.savefig("charts/profit_margin.png")
plt.show()

# Region-wise Sales Analysis

region_sales = df.groupby("Region")["Sales"].sum()

print("Region-wise Sales:")
print(region_sales.sort_values(ascending=False))

# Region-wise Sales Graph

plt.figure(figsize=(8, 5))

plt.bar(region_sales.index, region_sales.values)

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("charts/region_sales.png")

plt.show()

# Region-wise Profit Analysis

region_profit = df.groupby("Region")["Profit"].sum()

print("Region-wise Profit:")
print(region_profit.sort_values(ascending=False))

# Region-wise Profit Graph

plt.figure(figsize=(8, 5))

plt.bar(region_profit.index, region_profit.values)

plt.title("Profit by Region")

plt.xlabel("Region")

plt.ylabel("Total Profit")

plt.tight_layout()

plt.savefig("charts/region_profit.png")

plt.show()
# Region-wise Profit Margin

region_margin = (region_profit / region_sales) * 100

print("Region-wise Profit Margin:")
print(region_margin.sort_values(ascending=False))

# Region-wise Profit Margin Graph

plt.figure(figsize=(8, 5))

plt.bar(region_margin.index, region_margin.values)

plt.title("Profit Margin by Region")

plt.xlabel("Region")

plt.ylabel("Profit Margin (%)")

plt.tight_layout()
plt.savefig("charts/region_profit_margin.png")
plt.show()

# Region-wise Category Sales Analysis

region_category_sales = df.groupby(["Region", "Category"])["Sales"].sum()

print("Region-wise Category Sales:")
print(region_category_sales)
# Region-wise Category Sales Graph

region_category_sales.unstack().plot(kind="bar",figsize=(10, 6))

plt.title("Sales by Region and Category")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/region_category_sales.png")
plt.show()

# Region-wise Category Profit Analysis

region_category_profit = df.groupby(["Region", "Category"])["Profit"].sum()

print("Region-wise Category Profit:")
print(region_category_profit)

# Region-wise Category Profit Graph

region_category_profit.unstack().plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Profit by Region and Category")
plt.xlabel("Region")
plt.ylabel("Total Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/region_category_profit.png")
plt.show()

# Region-wise Category Profit Margin

region_category_margin = (
    region_category_profit / region_category_sales
) * 100

print("Region-wise Category Profit Margin:")
print(region_category_margin)

# Region-wise Category Profit Margin Graph

region_category_margin.unstack().plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Profit Margin by Region and Category")
plt.xlabel("Region")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/region_category_profit_margin.png")
plt.show()
# Overall Project Summary

print("Total Sales:", total_sales)
print("Total Profit:", total_profit)

print("\nBest Sales Region:")
print(region_sales.idxmax())

print("\nBest Profit Region:")
print(region_profit.idxmax())

print("\nBest Sales Category:")
print(category_sales.idxmax())

print("\nBest Profit Category:")
print(category_profit.idxmax())
# Overall Profit Margin

overall_profit_margin = (total_profit / total_sales) * 100

print("\nOverall Profit Margin:", overall_profit_margin, "%")

