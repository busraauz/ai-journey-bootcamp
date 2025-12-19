
# Day 3 - Online Retail Pandas Analysis: Customer Segmentation

## Objective
Spot my most valuable e-commerce customers, understand how often (and how recently) they buy, and quantify the revenue that is concentrated in high-value or at-risk cohorts using the same pandas-based workflow as Days 1-2.

## Dataset
UCI Online Retail (2009-2011) downloaded via `datasets/download.py` and stored at `datasets/online_retail.csv`. After dropping rows without `Customer ID`, enforcing positive `Price`/`Quantity`, and trimming price outliers with an IQR fence (Q1=GBP 1.25, Q3=GBP 3.75), I analyzed 738,203 transactions made by 5,819 customers worth GBP 15.25M.

## Key Techniques
- Baseline pandas hygiene: dtype fixes, chained filtering, derived columns (`Total Price`, calendar splits), and seaborn/matplotlib visuals for boxplots, distributions, and heatmaps.
- Manual IQR-based price filtering before aggregations to avoid gift-set anomalies that distort average spend per customer.
- Multi-pass customer aggregations built from `groupby().agg()` to derive repeat-vs-single counts, top-decile revenue share, purchase gaps, revenue tiers, and recency labels.
- Successive merges of frequency, revenue, and recency tables to create a master segmentation grid for downstream heatmaps and \"revenue at risk\" views.

## Key Insights
- Repeat buyers dominate: 4,209 multi-invoice customers (72%) generate GBP 14.76M, or 96.8% of all cleaned revenue; single-order shoppers contribute only GBP 0.49M.
- Revenue is concentrated: the top 10% of customers control GBP 9.82M (64.4%) of in-period revenue even after clipping high-price outliers.
- Purchase cadence varies wildly: the \"Low Frequency\" bucket (short-gap buyers) repeats roughly every 28 days, whereas the \"High Frequency\" bucket (long-gap buyers) takes ~207 days-so the naming in the notebook needs clarification.
- Recency health check: 1,942 \"Active\" customers repurchased within ~16 days, 1,898 are \"Warm\" (~115 days), and 1,979 sit in \"Churn Risk\" with ~460-day dormancy.
- Only GBP 111K of revenue comes from high-revenue, high-cadence customers who now look like churn risks, indicating an actionable but contained win-back list.

## Business Questions Answered
- How much of my revenue is controlled by repeat buyers versus one-off shoppers?
- What share of revenue is locked inside the top decile of the customer base, and how unequal is the distribution?
- Which customer frequency/revenue intersections are most common, and where do high-value clients show declining recency?
- How big is the \"revenue at risk\" pool if I focus on high-revenue customers who have slowed down dramatically?

## What I Learned
- Recreating the full segmentation pipeline in pandas (clean -> feature -> aggregate -> merge -> visualize) exposed the importance of consistent bin definitions-especially when multiple segment labels (frequency by gap vs. invoice count) coexist.
- Building joins from tidy intermediary tables keeps the notebook readable and avoids deeply nested `groupby` expressions when preparing visuals such as the frequency x revenue heatmap.
