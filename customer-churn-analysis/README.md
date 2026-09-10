# Customer Churn Analysis

## Project Overview

This project analyzes customer churn patterns using Python, Pandas, and Matplotlib. The goal is to understand which customer groups show higher churn rates and identify patterns that can support customer-retention decisions.

## Business Questions

1. What percentage of customers churn?
2. Which contract type has the highest churn rate?
3. Which internet service group has the highest churn rate?
4. Is churn different between customers with and without technical support?
5. How does churn vary by payment method?
6. How do monthly charges and customer tenure differ between churned and retained customers?
7. Which age and tenure groups show higher churn rates?

## Dataset

The dataset contains customer-level information including:

- Customer ID
- Age
- Tenure in months
- Monthly charges
- Contract type
- Internet service
- Technical support
- Payment method
- Churn status

## Tools & Technologies

- Python
- Pandas
- Matplotlib
- GitHub

## Analysis Performed

### Data Quality Checks

- Inspected the first rows and dataset shape
- Checked column names and data types
- Checked missing values
- Checked duplicate rows
- Checked duplicate customer IDs

### Exploratory Analysis

- Overall churn rate
- Churn rate by contract type
- Churn rate by internet service
- Churn rate by technical support
- Churn rate by payment method
- Average monthly charges by churn status
- Average tenure by churn status
- Churn rate by age group
- Churn rate by tenure group

### Visualizations

The Python script generates these charts:

- `churn_by_contract.png`
- `churn_by_internet_service.png`
- `churn_by_tech_support.png`
- `churn_by_payment_method.png`
- `churn_by_age_group.png`
- `churn_by_tenure_group.png`

## Key Analytical Approach

Churn rate is calculated as the percentage of customers with `Churn = Yes` within each group. Groups are compared using the same metric so that differences in customer counts do not distort the comparison.

## Business Interpretation

The analysis is designed to help a business identify customer segments with relatively high churn. Higher churn in a segment can indicate an area that deserves further investigation, such as contract structure, service experience, payment behavior, or customer tenure.

The findings should be treated as **associations rather than proof of causation**. A higher churn rate in a group does not by itself prove that the group's characteristic causes customers to leave.

## How to Run

Open a terminal inside the `customer-churn-analysis` folder and run:

```bash
py churn_analysis.py
```

The script prints the analysis results and opens the charts one by one. Close each chart window to continue to the next analysis.

## Project Structure

```text
customer-churn-analysis/
├── churn_analysis.py
├── churn_data.csv
├── requirements.txt
└── README.md
```

## Portfolio Note

This project demonstrates practical data analyst skills including data inspection, data-quality checking, grouping and aggregation with Pandas, churn-rate analysis, visualization with Matplotlib, and business-oriented interpretation.
