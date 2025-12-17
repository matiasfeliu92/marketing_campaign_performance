import logging
import pandas as pd
import platform

from src.config.settings import Settings
from src.config.db import ManageDB

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

class Load:
    def __init__(self):
        self.settings = Settings()
        self.manage_db = ManageDB()
        self.conn_string_default_DB = self.settings.POSTGRES_CONNECTION_STRING_DEFAULT_DB if platform.system() == "Windows" else self.settings.POSTGRES_CONNECTION_STRING_DOCKER_DEFAULT_DB
        self.conn_string_for_cursor_default_DB = self.settings.POSTGRES_CURSOR_CONNECTION_STRING_DEFAULT_DB if platform.system() == "Windows" else self.settings.POSTGRES_CURSOR_CONNECTION_STRING_DOCKER_DEFAULT_DB
        self.engine = None
        self.conn_string_new_DB = self.settings.POSTGRES_CONNECTION_STRING_NEW_DB if platform.system() == "Windows" else self.settings.POSTGRES_CONNECTION_STRING_DOCKER_NEW_DB
        self.conn_string_for_cursor_new_DB = self.settings.POSTGRES_CURSOR_CONNECTION_STRING_NEW_DB if platform.system() == "Windows" else self.settings.POSTGRES_CURSOR_CONNECTION_STRING_DOCKER_NEW_DB

    def load_data_in_DB(self, __df__: pd.DataFrame):
        logging.info(f"-------CONNECT USING {self.conn_string_for_cursor_default_DB}-------")
        connection = self.manage_db.create_connection(self.conn_string_for_cursor_default_DB)
        if connection is not None:
            self.manage_db.create_database(connection, self.settings.POSTGRES_DB_NAME_USE)
            logging.info(f"-------CONNECT TO CREATED DB USING {self.conn_string_for_cursor_new_DB}-------")
            new_connection = self.manage_db.create_connection(self.conn_string_for_cursor_new_DB)
            if new_connection is not None:
                self.manage_db.create_schema(new_connection, self.settings.POSTGRES_DB_SCHEMA_RAW)
                logging.info(f"-------CREATE ENGINE USING {self.conn_string_new_DB}-------")
                self.engine = self.manage_db.create_engine(self.conn_string_new_DB)
                if not __df__.empty:
                    logging.info(f"EL DATAFRAME POSEE {__df__.shape[0]} FILAS")
                    schema = self.settings.POSTGRES_DB_SCHEMA_RAW
                    table_name = "marketing_campaign_performance"
                    with self.engine.connect() as conn:
                        __df__.to_sql(
                            table_name, conn, schema=schema, if_exists="replace", index=False
                        )
                        logging.info(
                            f"Table {table_name} was saved in {self.settings.POSTGRES_DB_NAME_USE}.{schema}"
                        )