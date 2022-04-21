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
    if GENDER not in df:
        df.insert(loc=0, column=GENDER, value='0')
    
    if FIRST_NAME not in df:
        df.insert(loc=0, column=FIRST_NAME, value='prenom a renseigner')
    else:
        df[FIRST_NAME] = df[FIRST_NAME].fillna('A')
    
    if COUNTRY not in df:
        df.insert(loc=0, column=COUNTRY, value='FR')
    else:
        df[COUNTRY] = df[COUNTRY].astype(str)
        df[COUNTRY] = df[COUNTRY].replace(['FRANCE', 'france', 'France'], 'FR')
        df[COUNTRY] = df[COUNTRY].replace(['nan'], 'N/A')
    
    if CITY not in df:
        df.insert(loc=0, column=CITY, value='N/A')
    if ZIP not in df:
        df.insert(loc=0, column=ZIP, value='N/A')
    if ADDRESS not in df:
        df.insert(loc=0, column=ADDRESS, value='N/A')
    if STREET not in df:
        df.insert(loc=0, column=STREET, value='N/A')
    if NUMBER not in df:
        df.insert(loc=0, column=NUMBER, value='N/A')
    if DATE_OF_BIRTH not in df:
        df.insert(loc=0, column=DATE_OF_BIRTH, value='N/A')
    
    if MOBILE not in df:
        df.insert(loc=0, column=MOBILE, value='')
    else:
        df[MOBILE] = df[MOBILE].fillna('')

    if EMAIL not in df:
        df.insert(loc=0, column=EMAIL, value='N/A')
    else:
        df[EMAIL] = df[EMAIL].fillna('N/A')

    return df