import pandas as pd
import numpy as np
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import path





class DataIngestion:
    def __init__(self):
        pass
    def initialize_data_ingestion(self):
        logging.info("data_ingestion started")

        try:
            pd.read_csv(path(os.path.join("notebooks/data","gemstone.csv")))
        except Exception as e:
            pass