# Day 5 - Online Retail Pandas Cohort Analysis

## Objective
Identify which acquisition months deliver sticky customers, quantify post-purchase decay, and spotlight cohorts that need win-back campaigns by building a retention matrix from the cleaned Online Retail dataset.

## Dataset
UCI Online Retail (2009-2011) from `datasets/online_retail.csv`. I reused the Day 3 cleaning recipe: drop missing `Customer ID`, enforce positive `Price`/`Quantity`, and filter price outliers via the IQR fence (Q1=GBP 1.25, Q3=GBP 3.75). The trimmed table covers 738,203 line items (36,057 invoices) from 5,819 customers spread across 25 month-based cohorts.

## Key Techniques
- Feature engineering of first-purchase timestamps per customer via `groupby` + `min`, followed by `.dt.to_period("M")` to label cohorts cleanly.
- Calculating cohort age with month deltas to assign a `Cohort Index`, then constructing a cohort matrix with `pivot(index="Cohort Month", columns="Cohort Index")`.
- Deriving retention by dividing each column by the cohort's month-1 population and visualizing the result with a seaborn heatmap for fast pattern recognition.
- Executive scoring layer: `Health Score = 0.5*M1 + 0.3*M2 + 0.2*M3` to rank cohorts, plus `diff(axis=1)` to measure drop-off velocity month over month.

## Key Insights
- Acquisition volume skews early: December 2009 brought in 944 first-time customers, dwarfing late-period cohorts such as December 2011 (28 customers), so every retention point in early cohorts is worth far more revenue.
- Retention cliff: although Month 1 retention is 100% by definition, the average drops to 20.9% in Month 2 (-79 percentage points) and hovers near 22% by Month 3, underscoring how most customers churn immediately after the first purchase.
- Best performers: December 2009, September 2011, and August 2011 cohorts post health scores of 0.67, 0.65, and 0.64 respectively thanks to 26%-38% Month 3 retention, showing that late-2011 acquisition pushes were effective despite smaller volumes.
- Worst performers: November 2011, December 2010, and December 2011 collapse below a 0.55 health score, with holiday buyers in 2011-November falling to 0% retention by Month 3-prime candidates for early January win-back emails.
- Long-tail heartbeat: despite steep early decay, average retention drifts back above 20% around Month 21-24, suggesting yearly replenishment cycles from a loyal minority worth nurturing.

## Business Questions Answered
- Which acquisition months (cohorts) bring the most customers, and how concentrated is that volume?
- How quickly do cohorts decay, and in which month do we lose the majority of customers?
- Which cohorts should sales and retention teams prioritize because they either outperform (to replicate) or underperform (to rescue)?
- Do dormant customers ever reappear in later months, or is churn final after the initial drop?

## What I Learned
- Building cohorts directly inside pandas (first purchase lookup -> merge -> period pivot) keeps the analysis reproducible without extra SQL or BI tooling.
- Layering simple scoring (weighted Month 1-3 retention) on top of the raw retention matrix makes it far easier to communicate which cohorts need action than showing a heatmap alone.
- Tracking average drop-off via `.diff()` exposed the brutal Month 1->2 cliff immediately, reinforcing why day-30 engagement programs are table stakes for this retailer.
