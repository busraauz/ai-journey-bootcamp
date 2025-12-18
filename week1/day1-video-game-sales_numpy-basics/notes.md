# Day 1 – Video Game Sales __ NumPy Basics

## Objective
Use NumPy-first workflows to explore the global video game market and practice cleaning, aggregating, and visualizing structured numeric data without relying on pandas.

## Dataset
Video Game Sales (`gregorut/videogamesales` on Kaggle): 16.6k titles spanning 1980–2017 with platform, publisher, genre, and regional sales (in millions of units) that were downloaded locally via the `datasets/download.py` helper.

## Key Techniques
- `numpy.genfromtxt` to load the CSV into structured arrays with typed columns
- Boolean masking and `np.sum`/`np.mean` aggregations for per-genre and per-region rollups
- Axis-based slicing to build yearly sales vectors for trend charts
- Quick `matplotlib` line and bar visualizations exported to `outputs/`

## Key Insights
- Industry demand peaked in the late 2000s, with 2008 reaching roughly **679M** units sold worldwide.
- Platform and Shooter games lead on a per-title basis, averaging **0.94M** and **0.79M** global units respectively.
- North America contributes the highest average units per release (~**0.26M**), followed by Europe (**0.15M**) and Japan (**0.08M**), highlighting region-specific go-to-market strategies.

## Business Questions Answered
- Which release years delivered the strongest global revenue momentum?
- What genres generate the highest average global sales per launch?
- Which geographic regions drive the majority of unit sales for an average title?

## What I Learned
- Reinforced comfort with NumPy I/O patterns (skipping headers, defining dtypes, handling `N/A` years).
- Boolean masks stay readable when broken into intent-revealing helper arrays before aggregations.
- Verifying NumPy aggregations against Matplotlib annotations helps catch silent type/axis mistakes early.
