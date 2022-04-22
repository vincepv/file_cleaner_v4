import pandas as pd

def clean_zip_fr(clean_zip_df):
    
    
    df = clean_zip_df.copy()
    df['cp'] = df['cp'].fillna('N/A')
    df['cp'] = df['cp'].astype(str)
    df['cp'] = df['cp'].str.replace('\.0$', '', regex=True)
    clean_zip_done = df['cp']
    
    return clean_zip_done