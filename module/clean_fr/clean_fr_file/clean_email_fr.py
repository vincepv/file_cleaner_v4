import pandas as pd

def clean_email_fr(clean_email_df):
    
    
    df = clean_email_df.copy()
    df['email'] = df['email'].astype(str)
    
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

    df['email'] = df['email'].replace(dic_email, regex=True)
    df['email'] = df['email'].replace('nan', '')
    df['email'] = df['email'].str.strip()
    df['email'] = df['email'].str.lower()
    df.loc[df['email'].duplicated(), ['email']] = ''
    
    clean_email_fr_done = df['email']
    return clean_email_fr_done