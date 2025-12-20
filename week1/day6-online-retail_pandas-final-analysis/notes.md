# Day 6 - Online Retail Pandas Final Analysis

## Objective
Run a four-level analytics pass (Descriptive → Diagnostic → Predictive → Prescriptive) on the Online Retail dataset so Day 7 can reuse a single, battle-tested workflow for any new data source.

## Dataset
UCI Online Retail (2009-2011) sourced from `datasets/online_retail.csv`. I repeated the standard hygiene: drop missing `Customer ID`, enforce positive `Price`/`Quantity`, and filter prices via the IQR fence (Q1=GBP 1.25, Q3=GBP 3.75). The cleaned table holds 738,203 rows (36,057 invoices) from 5,819 customers worth GBP 15.25M.

## Key Techniques
- **Descriptive:** `resample("D"/"W")` plus KPI aggregations (total revenue, unique invoices/customers, average vs. median day) to capture “what happened” at a glance.
- **Diagnostic:** Dual-axis segmentation by invoice frequency and per-order revenue using quantile cutoffs, producing a 3×3 matrix that reveals who drives revenue and where churn risk concentrates.
- **Predictive:** Simple linear regression over the last 12 weekly revenue points to project near-term sales, paired with cohort-average retention curves to approximate lifetime value.
- **Prescriptive:** Recency buckets (Active/Warm/Churn Risk) and segment-level action notes that tie the previous three layers to concrete win-back or growth plays.

## Key Insights
- **Descriptive:** Total cleaned revenue hits GBP 15.25M; the average day earns GBP 25.2K (median GBP 21.7K) but 9 Dec 2011 spiked to GBP 182.7K. The week of 5 Dec 2011 delivered GBP 380K, a 70% jump over the prior week thanks to holiday demand.
- **Diagnostic:** High-frequency & high-revenue customers (895 people) account for GBP 9.87M (~65% of revenue). Another 1,201 customers sit in “High Revenue but Low/Medium Frequency” and generate GBP 1.49M—prime upsell targets. Low-frequency & low-revenue shoppers (1,069 customers) barely add GBP 0.16M.
- **Predictive:** A regression on the last 12 weekly totals forecasts GBP ~273K for the next week, implying holiday momentum should stay above the 12-week average (GBP 245K) even if it cools after the peak. Cohort retention averages 20.9% by Month 2 and 18.9% by Month 6; using the observed retention curve, per-customer CLTV approximates GBP 14.2K.
- **Prescriptive:** Recency split shows 1,942 Active, 1,898 Warm, and 1,979 Churn-Risk customers. That Churn-Risk pool overlaps heavily with low-frequency cohorts, so Day 7 should pilot win-back offers for the “High Revenue, High Frequency but Aging” slice before their contribution deteriorates.

## Business Questions Answered
- How volatile is daily/weekly revenue, and which recent weeks outperform the historical baseline?
- Which customer segments (frequency × revenue) carry most of the business, and which segments are both small and unprofitable?
- Given the latest 12-week trend, what revenue should leadership expect next week if conditions stay similar?
- Which customer groups deserve proactive outreach versus watch-and-see monitoring based on recency and cohort decay?

## What I Learned
- Structuring the notebook around the four analytics levels keeps the narrative tight: each section flows naturally into the next set of charts.
- Even lightweight predictive steps (rolling means + linear regression) give enough forward-looking context to justify prescriptive recommendations.
- Re-using the cleaned dataset and segmentation thresholds from prior days saves hours; Day 7 can now plug in a new CSV and follow the same blueprint with confidence.
