import pandas as pd
from config import EMAIL

def clean_email_fr(clean_email_df):
    
    
    df = clean_email_df.copy()
    df[EMAIL] = df[EMAIL].astype(str)
    
    dic_email = {
        'à': 'a',
        ',': '.',
        ';': '.',
        'ç': 'c',
        'é': 'e',
        'è': 'e',
        '@@':'@',
        '<':'',
        '>':'',
        
        }

    df[EMAIL] = df[EMAIL].replace(dic_email, regex=True)
    df[EMAIL] = df[EMAIL].replace('nan', '')
    df[EMAIL] = df[EMAIL].str.strip()
    df[EMAIL] = df[EMAIL].str.lower()
    df.loc[df[EMAIL].duplicated(), [EMAIL]] = ''
    
    clean_email_fr_done = df[EMAIL]
    return clean_email_fr_done