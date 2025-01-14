import pandas as pd

import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Define dataset path
dataset = "hmavrodiev/london-bike-sharing-dataset"
download_path = "datasets/london_bike_sharing"

# Download dataset
os.makedirs(download_path, exist_ok=True)
api.dataset_download_files(dataset, path=download_path, unzip=True)

#print(f"Dataset downloaded and extracted to: {download_path}")

#read in the csv file as a dataframe
bikes = pd.read_csv("datasets/london_bike_sharing/london_merged.csv")


#explore the data
#bikes.info()

print(bikes.head())




