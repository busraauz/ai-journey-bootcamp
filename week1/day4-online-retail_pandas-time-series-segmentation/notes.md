# Day 4 - Online Retail Pandas Time-Series Segmentation

## Objective
Track the ebb and flow of revenue and active customers for the UK gift retailer, highlight seasonality spikes, and spot soft spots that need follow-up by leaning on pandas resampling and smoothing techniques.

## Dataset
UCI Online Retail (2009-2011) accessed via `datasets/online_retail.csv`. After removing rows without `Customer ID`, forcing positive `Price`/`Quantity`, and clipping outlier prices with an IQR fence (Q1=GBP 1.25, Q3=GBP 3.75), I analyzed 738,203 transactions from 5,819 customers totaling GBP 15.25M, identical to the cleaning pipeline on Day 3 so the segmentations stay consistent.

## Key Techniques
- Time-aware aggregation with `set_index("InvoiceDate")` plus `.resample("D"|"W"|"ME")` to create daily, weekly, and month-end revenue series in only a few lines.
- Temporal feature engineering using `.dt.day_name()`/`.dt.month_name()` and ordered categoricals to build readable weekday/month activity charts.
- Customer activity tracking with `.resample(...).nunique()` to count active customers, followed by `.rolling(window=7/30).mean()` to smooth noisy holiday swings.
- Side-by-side matplotlib subplots (daily vs weekly, weekday vs month, raw vs rolling) to make multiple time scales comparable without duplicating prep work.

## Key Insights
- Holidays dominate: the single biggest day (9 Dec 2011) delivered GBP 182.7K, roughly 7x the GBP 25.2K daily average, and the week starting 5 Dec 2011 cleared GBP 380K.
- November 2011 became the best month (GBP 1.02M) while February 2011 sagged to GBP 0.38M, underscoring how post-holiday lulls drag quarterly totals.
- Thursdays drive the order book (7,570 unique invoices) whereas Saturdays barely register (29 invoices), signaling a weekday-heavy, probably B2B demand mix.
- Daily active customers peaked at 131 on 25 Nov 2010; by late 2011 the 7-day rolling average climbed to ~104 customers/day, confirming sustained holiday growth across cohorts even when individual days whipsaw.
- Weekly active customers topped out at 562 during the week of 14 Nov 2011, and the 30-day rolling view shows the year-long mid-2010 plateau giving way to a steeper climb heading into Q4 2011.

## Business Questions Answered
- When do revenue and customer counts spike versus slump across daily, weekly, and monthly time scales?
- Which weekdays and months contribute the most invoices, and are weekends worth staffing?
- How quickly do active customer counts recover after peak season, and where should retention teams expect soft patches?
- Does smoothing (7-day and 30-day rolling windows) confirm that Q4 holiday lifts are structural or just isolated spikes?

## What I Learned
- Resampling plus rolling windows gives a compact yet expressive toolkit for zooming between granular and strategic time horizons without rewriting logic each time.
- Adding ordered categoricals for calendar labels prevents matplotlib from scrambling weekday/month order, making the resulting visuals tell a cleaner story.
- Aligning the Day 4 notebook with Day 3's cleaning steps keeps every downstream metric (revenue and active customer counts) directly comparable, which is crucial when layering segmentation and time-series analyses in later days.
