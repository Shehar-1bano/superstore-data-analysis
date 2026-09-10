import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("churn_data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

# Overall churn rate
churn_rate = df["Churn"].eq("Yes").mean() * 100
print(f"\nOverall churn rate: {churn_rate:.2f}%")

# Churn by contract
contract_churn = df.groupby("Contract")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
print("\nChurn rate by contract:")
print(contract_churn)

contract_churn.plot(kind="bar", title="Churn Rate by Contract")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Contract Type")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_contract.png")
plt.show()

# Churn by internet service
internet_churn = df.groupby("InternetService")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
print("\nChurn rate by internet service:")
print(internet_churn)

internet_churn.plot(kind="bar", title="Churn Rate by Internet Service")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Internet Service")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_internet_service.png")
plt.show()

# Churn by tech support
support_churn = df.groupby("TechSupport")["Churn"].apply(lambda x: (x == "Yes").mean() * 100).sort_values(ascending=False)
print("\nChurn rate by tech support:")
print(support_churn)

support_churn.plot(kind="bar", title="Churn Rate by Tech Support")
plt.ylabel("Churn Rate (%)")
plt.xlabel("Tech Support")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("churn_by_tech_support.png")
plt.show()

# Average monthly charges by churn status
avg_charges = df.groupby("Churn")["MonthlyCharges"].mean()
print("\nAverage monthly charges by churn status:")
print(avg_charges)

# Average tenure by churn status
avg_tenure = df.groupby("Churn")["TenureMonths"].mean()
print("\nAverage tenure by churn status:")
print(avg_tenure)

# Key business insights
print("\nKey insights:")
print(f"- Overall churn rate is {churn_rate:.2f}%.")
print(f"- Highest churn contract: {contract_churn.index[0]} ({contract_churn.iloc[0]:.2f}%).")
print(f"- Highest churn internet service: {internet_churn.index[0]} ({internet_churn.iloc[0]:.2f}%).")
print(f"- Highest churn support group: {support_churn.index[0]} ({support_churn.iloc[0]:.2f}%).")
