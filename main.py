from src.scripts.extract import Extract
from src.scripts.load import Load

if __name__ == "__main__":
    extract = Extract()
    df_extracted = extract.extract_file_from_kaggle()
    load = Load()
    load.load_data_in_DB(df_extracted)