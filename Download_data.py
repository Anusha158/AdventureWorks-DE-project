# download_data.py
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files(
    "zynicide/wine-reviews",
    path="data",
    unzip=True
)
