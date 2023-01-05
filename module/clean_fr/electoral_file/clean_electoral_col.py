import pandas as pd
from config import *

def clean_electoral_col(my_dataframe):
    
    df = my_dataframe.copy()

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

    return df