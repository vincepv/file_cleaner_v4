import pandas as pd
from config import *

def create_column(func):
  def wrapper():
    if CATEGORY not in df:
        df.insert(loc=0, column=CATEGORY, value='3')
    if NOTE not in df:
        df.insert(loc=0, column=NOTE, value='')
    if KEYWORD not in df:
        df.insert(loc=0, column=KEYWORD, value='')
    
    if COUNTRY not in df:
        df.insert(loc=0, column=COUNTRY, value='FR')
    else:
        df[COUNTRY] = df[COUNTRY].astype(str)
        df[COUNTRY] = df[COUNTRY].replace(['FRANCE', 'france', 'France'], 'FR')
        df[COUNTRY] = df[COUNTRY].replace(['nan'], '')
    
    if MOBILE not in df:
        df.insert(loc=0, column=MOBILE, value='')
    else:
        df[MOBILE] = df[MOBILE].fillna('')

    if EMAIL not in df:
        df.insert(loc=0, column=EMAIL, value='')
    else:
        df[EMAIL] = df[EMAIL].fillna('')
    func()
  return wrapper


@create_column
def creation_col_x():
  print('colonne X')

creation_col_x()