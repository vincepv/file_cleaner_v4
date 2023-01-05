import pandas as pd
from config import FIRST_NAME, LAST_NAME, ORGANISATION

def clean_empty_name_fr(clean_empty_name_column):
    
    """
    Fill empty firstname and lastname with organisation
    """
    
    df = clean_empty_name_column.copy()
    
    if ORGANISATION in df:
        df[LAST_NAME] = df[LAST_NAME].fillna(df[ORGANISATION])
        df[FIRST_NAME] = df[FIRST_NAME].fillna(df[ORGANISATION])

    dic_organisme_clean = {
        '\'':' ',
        '^ ':'',
        '\d': '',
        '\.': '',
        '&': 'et',
        '\(':'',
        '\)':'',
        '-':'',
        'à':'',
        '/':' ',
        ',':'',
        '(?<=^.{45}).+':'',
    }
    
    df[[LAST_NAME,FIRST_NAME]] = df[[LAST_NAME,FIRST_NAME]].replace(dic_organisme_clean, regex=True)
    clean_empty_name_done  = df[[LAST_NAME,FIRST_NAME]]
    return clean_empty_name_done