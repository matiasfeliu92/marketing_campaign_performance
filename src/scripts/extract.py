import logging
import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi

from src.config.settings import Settings

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class Extract:
    def __init__(self):
        self.settings = Settings()
        self.kaggle_username = self.settings.KAGGLE_USERNAME
        self.kaggle_api_key = self.settings.KAGGLE_KEY
        self.api = KaggleApi()

    def extract_file_from_kaggle(self):
        if not self.kaggle_username or not self.kaggle_api_key:
            raise ValueError("Las variables de entorno KAGGLE_USERNAME o KAGGLE_KEY no están definidas.")
        os.environ['KAGGLE_USERNAME'] = self.kaggle_username
        os.environ['KAGGLE_KEY'] = self.kaggle_api_key
        self.api.authenticate()
        logging.info("Conexión a Kaggle exitosa.")
        self.api.dataset_download_files(
            dataset="manishabhatt22/marketing-campaign-performance-dataset", 
            path='/tmp/', 
            unzip=True
        )
        df_downloaded = pd.read_csv('/tmp/marketing_campaign_dataset.csv', encoding='ISO-8859-1')
        logging.info(f"El dataset contiene {df_downloaded.shape[0]} filas")
        logging.info(df_downloaded.head())
        return df_downloaded