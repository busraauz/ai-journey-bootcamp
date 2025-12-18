# Day 2 – NYC Airbnb _ Pandas Basics

## Objective
Profile New York City Airbnb listings to understand how pricing, availability, and popularity vary by borough, room type, and price tier while reinforcing end-to-end pandas data-wrangling patterns.

## Dataset
NYC Airbnb Open Data (`dgomonov/new-york-city-airbnb-open-data` on Kaggle): 48,881 listings (2019 snapshot) with geography, host info, calendars, and review counts, downloaded via `datasets/download.py` and read from `datasets/airbnb_listings.csv`.

## Key Techniques
- `pandas.read_csv` with chained `drop`, `fillna`, and datetime parsing to tidy raw CSVs quickly.
- Feature engineering—`last_review_year`, `last_review_month`, and `availability_rate`—to make temporal and occupancy analysis easier.
- IQR-based price filtering plus `DataFrame.quantile` driven segmentation to remove extreme listings and build Low/Mid/High bands.
- `groupby` aggregations with vectorized arithmetic and seaborn/matplotlib visuals (histograms, count plots, heatmaps, bar charts) exported to `outputs/`.

## Key Insights
- Manhattan still commands the premium nightly rate (~$146) while Bronx listings trail at ~$77, signaling borough-specific pricing power gaps of ~90%.
- Entire homes/apartments sustain the highest occupancy (~71%) with private rooms close behind (~70%), but shared rooms lag at ~55%, implying weaker demand for budget shared inventory.
- Mid-priced listings (between the 33rd–66th percentiles) balance both utilization and buzz—~72% occupancy and ~27 reviews on average—whereas high-priced stays drop to ~67% occupancy and only ~22 reviews.

## Business Questions Answered
- Which neighbourhood groups deliver the highest and lowest average nightly rates?
- How do occupancy patterns differ across room types after adjusting for availability?
- What price bands maximize both occupancy and review volume (as a proxy for guest interest)?

## What I Learned
- Walking the full EDA loop end-to-end (inspect ➝ clean ➝ transform ➝ visualize ➝ analyze) keeps me honest about documenting each assumption instead of jumping straight to charts.
- Hands-on reps with bread-and-butter pandas moves—`df.drop`, chained `fillna`, vectorized arithmetic, and `df['new_col'] = ...`—make spinning up custom features second nature.
- `groupby` + `agg` workflows are incredibly flexible: the same pattern powered neighbourhood pricing, room-type occupancy, and price-tier review analysis with just a few argument tweaks.
