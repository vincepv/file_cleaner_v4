import pandas as pd
from config import my_pandas_folder


def athena_clean(my_file):
  df = pd.read_csv(my_file, low_memory=False)

  # select columns based on column_key, get line where cells are empty
  column_key = [ 'Email', 'Mobile', 'Numéro de rue', 'Nom de rue']
  df_empty_key = df.loc[df[column_key].isnull().all(axis=1)]

  # prepare data for merge
  # remove lines where all columns are empty
  df = df.dropna(subset=column_key, how='all')

  # merge df et df_empty_key on ['Prénom', 'Nom de naissance', 'Date de naissance']
  df_merged = pd.merge(df, df_empty_key, on=['Prénom', 'Nom de naissance', 'Date de naissance'], how='left', indicator=True, validate='m:m')
 

  # fusionne le contenu de Mots clés_y dans Mots clés_x
  df_merged['Mots clés_x'] = df_merged['Mots clés_x'].fillna('') + ',' + df_merged['Mots clés_y'].fillna('')
  # remove column ending with name _y
  df_merged = df_merged[df_merged.columns.drop(list(df_merged.filter(regex='_y')))]


  df_merged.to_csv(my_pandas_folder+"clean_athena.csv", header=True, index=False, encoding="utf8")