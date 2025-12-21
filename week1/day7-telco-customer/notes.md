# Day 7 - Telco Customer Churn Analysis

## Objective
Analyze churn drivers in the Telco Customer Churn dataset and summarize which customer attributes and services are most associated with churn.

## Dataset
Telco Customer Churn from `datasets/telco_customer_churn.csv` with 7,043 rows and 21 columns. Basic cleaning converts blank `TotalCharges` values to 0, casts `TotalCharges` to float, and binarizes Yes/No fields (Churn, Partner, Dependents, PhoneService, PaperlessBilling). Gender is encoded as F/M for charting.

## Key Techniques
- **Descriptive:** Dataset overview (`info`, `describe`, missing/duplicate checks) plus distributions for all categorical variables.
- **Diagnostic:** Grouped churn rates by contract, demographics, tenure, monetary value (TotalCharges), and service usage using normalized stacked bar charts.
- **Segmentation:** Quantile buckets for monetary value (3 bins) and tenure (5 bins) to compare churn across lifecycle stages.

## Key Insights
- **Contract:** Month-to-month customers churn the most (42.7%) vs one-year (11.3%) and two-year (2.8%).
- **Lifecycle/Value:** Churn drops with higher tenure (52.9% onboarding -> 6.6% long-term) and higher total charges (39.5% low -> 16.5% high).
- **Demographics:** Senior citizens churn more (41.7%) than non-seniors (23.6%); customers without partners (33.0%) or dependents (31.3%) churn more than those with them.
- **Services:** Internet/security/support choices show big gaps (fiber optic 41.9% vs DSL 19.0% vs no internet 7.4%; OnlineSecurity No 41.8% vs Yes 14.6%; TechSupport No 41.6% vs Yes 15.2%). PhoneService and streaming features have minor differences.

## Business Questions Answered
- Which contract types are highest risk for churn?
- How does churn change across tenure and customer value segments?
- Which demographic groups are more likely to churn?
- Which services are most associated with churn differences?

## What I Learned
- Simple churn-rate grouping surfaces strong signals quickly, especially by contract and tenure.
- Service-level features (internet/security/support) separate churn far more than basic phone or streaming add-ons.
- Combining tenure and monetary segments gives a clearer churn-risk ladder for retention targeting.
