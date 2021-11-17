import pandas as pd

def clean_address_fr(clean_address_df):
    df = clean_address_df.copy()
    
    df['adresse'] = df['adresse'].astype(str)
    df['adresse'] = df['adresse'].str.replace(',', '', regex=True)
    df['adresse'] = df['adresse'].replace('nan', '')
    df['adresse'] = df['adresse'].str.strip()
    
    clean_address_fr_done = df['adresse']
    
    return clean_address_fr_done