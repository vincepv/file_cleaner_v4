import pandas as pd
from config import ZIP

def clean_zip_fr(clean_zip_df):
    
    
    df = clean_zip_df.copy()
    df[ZIP] = df[ZIP].fillna('N/A')
    df[ZIP] = df[ZIP].astype(str)
    df[ZIP] = df[ZIP].str.replace('\.0$', '', regex=True)
    clean_zip_done = df[ZIP]
    
    return clean_zip_done