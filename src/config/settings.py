import os
import logging
from typing import List
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class Settings:
    BASE_DIR = os.getcwd()
    KAGGLE_USERNAME = os.getenv("KAGGLE_USERNAME")
    KAGGLE_KEY = os.getenv("KAGGLE_KEY")
    POSTGRES_DB_USER = os.getenv("DB_USER")
    POSTGRES_DB_PASS = os.getenv("DB_PASS")
    POSTGRES_DB_HOST = os.getenv("DB_HOST")
    POSTGRES_DB_HOST_DOCKER = os.getenv("DB_HOST_DOCKER")
    POSTGRES_DB_NAME = os.getenv("DB_NAME")
    POSTGRES_DB_NAME_USE = os.getenv("DB_NAME_USE")
    POSTGRES_CONNECTION_STRING_DEFAULT_DB = (
        f"postgresql+psycopg2://{POSTGRES_DB_USER}:{POSTGRES_DB_PASS}"
        f"@{POSTGRES_DB_HOST}:5432/{POSTGRES_DB_NAME}"
    )
    POSTGRES_CONNECTION_STRING_DOCKER_DEFAULT_DB = (
        f"postgresql+psycopg2://{POSTGRES_DB_USER}:{POSTGRES_DB_PASS}"
        f"@{POSTGRES_DB_HOST_DOCKER}:5432/{POSTGRES_DB_NAME}"
    )
    POSTGRES_CURSOR_CONNECTION_STRING_DEFAULT_DB = (
        "dbname={db} user={user} password={pwd} host={host} port={port}"
    ).format(
        db=POSTGRES_DB_NAME,
        user=POSTGRES_DB_USER,
        pwd=POSTGRES_DB_PASS,
        host=POSTGRES_DB_HOST,
        port=5432,
    )
    POSTGRES_CURSOR_CONNECTION_STRING_DOCKER_DEFAULT_DB = (
        "dbname={db} user={user} password={pwd} host={host} port={port}"
    ).format(
        db=POSTGRES_DB_NAME,
        user=POSTGRES_DB_USER,
        pwd=POSTGRES_DB_PASS,
        host=POSTGRES_DB_HOST_DOCKER,
        port=5432,
    )

    POSTGRES_CONNECTION_STRING_NEW_DB = (
        f"postgresql+psycopg2://{POSTGRES_DB_USER}:{POSTGRES_DB_PASS}"
        f"@{POSTGRES_DB_HOST}:5432/{POSTGRES_DB_NAME_USE}"
    )
    POSTGRES_CONNECTION_STRING_DOCKER_NEW_DB = (
        f"postgresql+psycopg2://{POSTGRES_DB_USER}:{POSTGRES_DB_PASS}"
        f"@{POSTGRES_DB_HOST_DOCKER}:5432/{POSTGRES_DB_NAME_USE}"
    )
    POSTGRES_CURSOR_CONNECTION_STRING_NEW_DB = (
        "dbname={db} user={user} password={pwd} host={host} port={port}"
    ).format(
        db=POSTGRES_DB_NAME_USE,
        user=POSTGRES_DB_USER,
        pwd=POSTGRES_DB_PASS,
        host=POSTGRES_DB_HOST,
        port=5432,
    )
    POSTGRES_CURSOR_CONNECTION_STRING_DOCKER_NEW_DB = (
        "dbname={db} user={user} password={pwd} host={host} port={port}"
    ).format(
        db=POSTGRES_DB_NAME_USE,
        user=POSTGRES_DB_USER,
        pwd=POSTGRES_DB_PASS,
        host=POSTGRES_DB_HOST_DOCKER,
        port=5432,
    )
    POSTGRES_DB_SCHEMA_RAW = os.getenv("DB_SCHEMA_RAW")

    def create_new_dir(self, path: List[str]):
        logging.info(f'-------NEW DIR ---> {os.path.join(self.BASE_DIR, *path)}-------')
        os.makedirs(os.path.join(self.BASE_DIR, *path), exist_ok=True)
        output_dir = os.path.join(self.BASE_DIR, *path)
        return output_dir
    
    def get_file_path(self, path: List[str], file_name):
        logging.info(f'-------FILE PATH ---> {os.path.join(self.BASE_DIR, *path, file_name)}-------')
        file_path = os.path.join(self.BASE_DIR, *path, file_name)
        return file_path