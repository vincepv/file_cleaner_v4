import pandas as pd
from config import KEYWORD

def clean_keyword_fr(clean_keyword_df):
    

    df = clean_keyword_df.copy()
    df[KEYWORD] = df[KEYWORD].fillna('')
    df[KEYWORD] = df[KEYWORD].astype(str)
    df[KEYWORD] = df[KEYWORD].str.replace('\.0$', '', regex=True)
    df[KEYWORD] = df[KEYWORD].str.upper()

    clean_delimitor = [
        ";",
        " ;",
        "; ",
        " ; ",
        " ,",
        ", ",
        " , "
    ]
    df[KEYWORD] = df[KEYWORD].replace(clean_delimitor, ',', regex=True)
    

    clean_leading_trailing =[
        "^,",
        ",$",
        "^;",
        ";$"
    ]
    df[KEYWORD] = df[KEYWORD].replace(clean_leading_trailing, '', regex=True)

    clean_keyword_done = df[KEYWORD]

    return clean_keyword_done