import kagglehub
from pathlib import Path
import shutil
BASE_DIR = Path(__file__).resolve().parents[1]
DATASET_DIR = BASE_DIR / "datasets"
DATASET_DIR.mkdir(exist_ok=True)

DATASETS = [
    {
        "name": "Video Game Sales",
        "kaggle_id": "gregorut/videogamesales",
        "source_file": "vgsales.csv",
        "target_file": "video_game_sales.csv",
    },
    {
        "name": "Airbnb Listings",
        "kaggle_id": "dgomonov/new-york-city-airbnb-open-data",
        "source_file": "AB_NYC_2019.csv",
        "target_file": "airbnb_listings.csv",
    },
    {
        "name": "Online Retail",
        "kaggle_id": "mashlyn/online-retail-ii-uci",
        "source_file": "online_retail_II.csv", 
        "target_file": "online_retail.csv",
    },
    {
        "name": "Telco Customer Churn",
        "kaggle_id": "blastchar/telco-customer-churn",
        "source_file": "WA_Fn-UseC_-Telco-Customer-Churn.csv", 
        "target_file": "telco_customer_churn.csv",
    },
    {
        "name": "Ames Housing Dataset",
        "kaggle_id": "prevek18/ames-housing-dataset",
        "source_file": "AmesHousing.csv", 
        "target_file": "ames_housing.csv",
    }
]

for ds in DATASETS:
    print(f"⬇️  Downloading: {ds['name']}")

    path = kagglehub.dataset_download(ds["kaggle_id"])
    source_path = Path(path) / ds["source_file"]
    target_path = DATASET_DIR / ds["target_file"]

    if not source_path.exists():
        raise FileNotFoundError(
            f"File not found in Kaggle dataset: {source_path}"
        )

    shutil.copy(source_path, target_path)
    print(f"✅ Saved to: {target_path}")

print("\n🎉 All datasets are ready.")
