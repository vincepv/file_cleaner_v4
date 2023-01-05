import pandas as pd
from config import *

def clean_column_fr(clean_column_df):
    """
    
    Add missing columns

    """
    
    df = clean_column_df.copy()
    
    if FIRST_NAME not in df:
        df.insert(loc=0, column=FIRST_NAME, value = None)

    if LAST_NAME not in df:
        df.insert(loc=0, column=LAST_NAME, value = None)

    if GENDER not in df:
        df.insert(loc=0, column=GENDER, value='0')

    if MOBILE not in df:
        df.insert(loc=0, column=MOBILE, value='')

    if ADDRESS not in df:
        df.insert(loc=0, column=ADDRESS, value='')
    
    if CITY not in df:
        df.insert(loc=0, column=CITY, value='')

    if ZIP not in df:
        df.insert(loc=0, column=ZIP, value='')
    
    if COUNTRY not in df:
        df.insert(loc=0, column=COUNTRY, value='FR')
    else:
        df[COUNTRY] = df[COUNTRY].astype(str)
        df[COUNTRY] = df[COUNTRY].replace(['FRANCE','france','France'],'FR')
        df[COUNTRY] = df[COUNTRY].replace(['nan'],'N/A')

    if CATEGORY not in df:
        df.insert(loc=0, column=CATEGORY, value='2')
    if NOTE not in df:
        df.insert(loc=0, column=NOTE, value='')
    if KEYWORD not in df:
        df.insert(loc=0, column=KEYWORD, value='')
    else:
        df[KEYWORD] = df[KEYWORD].str.strip(to_strip=",")
        
    if EMAIL not in df:
        df.insert(loc=0, column=EMAIL, value='')
        
    clean_column_done  = df

    return clean_column_done