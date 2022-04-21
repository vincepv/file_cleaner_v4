import pandas as pd
from config import COMMON_NAME, FIRST_NAME, BIRTH_NAME

def clean_name_electoral(my_dataframe):
    df = my_dataframe.copy()

    df[[FIRST_NAME,'other name']] = df[FIRST_NAME].str.split(' ',n=1, expand=True)
    df[FIRST_NAME] = df[FIRST_NAME].str.capitalize()
    df[COMMON_NAME] = df[COMMON_NAME].fillna(df[BIRTH_NAME])

    return df[[
        FIRST_NAME,
        'other name',
        COMMON_NAME
    ]]