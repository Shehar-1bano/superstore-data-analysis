import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("churn_data.csv")

print("CUSTOMER CHURN ANALYSIS")
print("=" * 40)

# Basic dataset checks
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
print("Duplicate Customer IDs:", df["CustomerID"].duplicated().sum())

# Overall churn
churn_count = (df["Churn"] == "Yes").sum()
retained_count = (df["Churn"] == "No").sum()
churn_rate = df["Churn"].eq("Yes").mean() * 100

print("\nOverall customer status:")
print("Churned customers:", churn_count)
print("Retained customers:", retained_count)
print(f"Overall churn rate: {churn_rate:.2f}%")

# Churn by contract
contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by contract:")
print(contract_churn.round(2))

contract_churn.plot(kind="bar", title="Churn Rate by Contract")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Contract Type")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_contract.png")
plt.show()

# Churn by internet service
internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by internet service:")
print(internet_churn.round(2))

internet_churn.plot(kind="bar", title="Churn Rate by Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Internet Service")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_internet_service.png")
plt.show()

# Churn by technical support
support_churn = df.groupby("TechSupport")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by technical support:")
print(support_churn.round(2))

support_churn.plot(kind="bar", title="Churn Rate by Technical Support")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Technical Support")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_tech_support.png")
plt.show()

# Churn by payment method
payment_churn = df.groupby("PaymentMethod")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by payment method:")
print(payment_churn.round(2))

payment_churn.plot(kind="bar", title="Churn Rate by Payment Method")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Payment Method")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig("churn_by_payment_method.png")
plt.show()

# Average monthly charges by churn status
avg_charges = df.groupby("Churn")["MonthlyCharges"].mean()

print("\nAverage monthly charges by churn status:")
print(avg_charges.round(2))

# Average tenure by churn status
avg_tenure = df.groupby("Churn")["TenureMonths"].mean()

print("\nAverage tenure by churn status:")
print(avg_tenure.round(2))

# Churn by age group
age_bins = [0, 30, 45, 60, 100]
age_labels = ["18-30", "31-45", "46-60", "61+"]
df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)

age_churn = df.groupby("AgeGroup", observed=True)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by age group:")
print(age_churn.round(2))

age_churn.plot(kind="bar", title="Churn Rate by Age Group")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Age Group")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_age_group.png")
plt.show()

# Churn by tenure group
tenure_bins = [-1, 12, 36, 60, 100]
tenure_labels = ["0-12 months", "13-36 months", "37-60 months", "61+ months"]
df["TenureGroup"] = pd.cut(df["TenureMonths"], bins=tenure_bins, labels=tenure_labels)

tenure_churn = df.groupby("TenureGroup", observed=True)["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
).sort_values(ascending=False)

print("\nChurn rate by tenure group:")
print(tenure_churn.round(2))

tenure_churn.plot(kind="bar", title="Churn Rate by Tenure Group")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Tenure Group")
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("churn_by_tenure_group.png")
plt.show()

# Business insights
print("\nKEY BUSINESS INSIGHTS")
print("=" * 40)
print(f"- Overall churn rate is {churn_rate:.2f}%.")
print(f"- Highest churn contract: {contract_churn.index[0]} ({contract_churn.iloc[0]:.2f}%).")
print(f"- Highest churn internet service: {internet_churn.index[0]} ({internet_churn.iloc[0]:.2f}%).")
print(f"- Highest churn support group: {support_churn.index[0]} ({support_churn.iloc[0]:.2f}%).")
print(f"- Highest churn payment method: {payment_churn.index[0]} ({payment_churn.iloc[0]:.2f}%).")
print(f"- Highest churn age group: {age_churn.index[0]} ({age_churn.iloc[0]:.2f}%).")
print(f"- Highest churn tenure group: {tenure_churn.index[0]} ({tenure_churn.iloc[0]:.2f}%).")

print("\nNote: These results describe associations in the dataset. They do not prove that a specific factor causes customer churn.")
