# Data Dictionary

| Column | Description |
|---|---|
| CustomerID | Unique customer identifier |
| Age | Customer age in years |
| TenureMonths | Number of months the customer has been with the company |
| MonthlyCharges | Customer's monthly service charge |
| Contract | Customer contract type |
| InternetService | Type of internet service |
| TechSupport | Whether the customer has technical support |
| PaymentMethod | Customer payment method |
| Churn | Whether the customer left the service (`Yes` or `No`) |

## Derived Fields

The analysis script creates two temporary fields:

- `AgeGroup`: age bands used to compare churn rates across age ranges.
- `TenureGroup`: tenure bands used to compare churn rates across customer lifecycle stages.
