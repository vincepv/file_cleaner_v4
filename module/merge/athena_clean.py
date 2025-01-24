import pandas as pd
from config import my_pandas_folder


def athena_clean(my_file):
  df = pd.read_csv(my_file, low_memory=False)

  # Drop columns
  column_key = [ 'Email', 'Mobile', 'Numéro de rue', 'Nom de rue']

  # copy line with column_key are empty to new dataframe
  

  # remove lines where all columns are empty
  df = df.dropna(subset=column_key, how='all')




  df.to_csv(my_pandas_folder+"clean_athena.csv", header=True, index=False, encoding="utf8")