import pandas as pd
from config import  my_pandas_folder, LAST_NAME ,ADDRESS ,ZIP


def unique_address(my_file):
    df = pd.read_csv(my_file, low_memory=False)
    df = df.drop_duplicates(
        subset=[LAST_NAME, ADDRESS,ZIP],
        keep='first')
    df.to_csv(my_pandas_folder+'DraftUniqueAddress.csv', header=True, index=False, encoding="utf8")