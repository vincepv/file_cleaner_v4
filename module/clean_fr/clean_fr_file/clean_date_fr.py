import pandas as pd

def clean_date_fr(clean_date_df):
    
    
    df = clean_date_df.copy()
    
    # consider date as str : dd-mm-yyyy    
    df['date'] = df['date'].astype(str)
    
    df.insert(loc=0, column='jour', value='N/A')
    df.insert(loc=0, column='mois', value='N/A')
    df.insert(loc=0, column='annee', value='N/A')
    
    df['jour'] = df['date'].str[:2]
    df['mois'] = df['date'].str[3:-5]
    df['annee'] = df['date'].str[6:]

    df['date'] = df['annee']+ "-" + df['mois']+ "-" + df['jour']
    # clean invalide date
    df['date'] = df['date'].replace(['--na', '--N/','--'], 'N/A', regex=True)
    
    df = df.drop(['jour', 'mois', 'annee'], axis=1)
    
    
    clean_date_done = df['date']
    return clean_date_done