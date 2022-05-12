import pandas as pd
import regex
from config import DATE_OF_BIRTH


def clean_date (my_dataframe):

  df = my_dataframe.copy()

  #clean false date format
  
  clean_value = {
    '^00':'01',
    '/00/':'/01/',
    '/0000$':'/2000',
  }


  df['clean_date'] = df[DATE_OF_BIRTH].replace(clean_value,regex=True)

  # convert yyyy-mm-dd
  df['clean_date'] = pd.to_datetime(
    df['clean_date'],
    errors='ignore',
    dayfirst=True,)

  return df['clean_date']