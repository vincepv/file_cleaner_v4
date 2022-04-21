import pandas as pd
from config import ADDRESS

def clean_address_fr(clean_address_df):
    df = clean_address_df.copy()
    
    df[ADDRESS] = df[ADDRESS].astype(str)
    df[ADDRESS] = df[ADDRESS].str.replace(',', '', regex=True)
    df[ADDRESS] = df[ADDRESS].replace('nan', '')
    df[ADDRESS] = df[ADDRESS].str.strip()
    
    clean_address_fr_done = df[ADDRESS]
    
    return clean_address_fr_done