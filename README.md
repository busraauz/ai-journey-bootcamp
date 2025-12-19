# AI Journey Bootcamp

Hands-on notebooks and notes for a five-day pandas analytics crash course. Every day focuses on a different dataset and technique stack.

## Week 1 Overview
| Day | Project | Focus | Outputs |
| --- | --- | --- | --- |
| 1 | Video Game Sales (NumPy basics) | Data cleaning, aggregations, plotting baseline | 3 PNG charts in `week1/day1-video-game-sales_numpy-basics/outputs/` |
| 2 | NYC Airbnb (Pandas basics) | Feature engineering, grouping, availability vs. price | 3 PNG charts in `week1/day2-nyc-airbnb _pandas-basics/outputs/` |
| 3 | Online Retail (Customer segmentation) | RFM-style cuts, frequency vs revenue heatmap | Notebook + `notes.md` + PNGs in `week1/day3-online-retail_pandas-customer-segmentation/outputs/` |
| 4 | Online Retail (Time-series segmentation) | Resampling, rolling averages, seasonal diagnostics | Notebook + `notes.md`  + PNGs in `week1/day4-online-retail_pandas-time-series-segmentation/outputs/` |
| 5 | Online Retail (Cohort analysis) | Month-based retention matrix, health scoring | Notebook + `notes.md` + PNGs in `week1/day5-online-retail_pandas-cohort-analysis/outputs/` |

## Getting Started
1. Create a Python 3 virtualenv and `pip install -r requirements.txt`.
2. All datasets live under `datasets/` (download via `python datasets/download.py` if needed).
3. Open any notebook in `week1/<day>/notebook.ipynb` to replay the analyses.

## Repo Layout
```
.
├── datasets/          # raw CSVs and downloader script
├── requirements.txt   # pandas, seaborn, matplotlib
├── week1/
│   ├── day1-video-game-sales_numpy-basics/
│   │   ├── notebook.ipynb
│   │   ├── notes.md
│   │   └── outputs/
│   ├── day2-nyc-airbnb _pandas-basics/
│   ├── day3-online-retail_pandas-customer-segmentation/
│   ├── day4-online-retail_pandas-time-series-segmentation/
│   └── day5-online-retail_pandas-cohort-analysis/
└── README.md
```
Each day folder contains an executable notebook, narrative notes, and (when relevant) saved charts in `outputs/`.
