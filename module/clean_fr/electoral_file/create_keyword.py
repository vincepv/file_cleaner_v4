import pandas as pd
from config import KEYWORD, POLLING_STATION


def create_keyword_electoral (my_dataframe):
    df = my_dataframe.copy()

    if POLLING_STATION in df:
        df[POLLING_STATION] = df[POLLING_STATION].astype(str)
        df[POLLING_STATION] = df[POLLING_STATION].str.replace('\.0$', '', regex=True)
        df[KEYWORD] = df[KEYWORD]+',BV '+df[POLLING_STATION]

    df[KEYWORD] = df[KEYWORD].astype(str)
    df[KEYWORD] = df[KEYWORD].replace('nan', '', regex=False)
    clean_keyword = {
        '\.0$':'',
        '^,':'',
        ',$':'',
        ';':',',
    }
    df[KEYWORD] = df[KEYWORD].replace(clean_keyword, regex=True)
    return df[KEYWORD]
