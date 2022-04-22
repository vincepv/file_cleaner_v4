import pandas as pd
from config import DATE_OF_BIRTH

def clean_date_fr(clean_date_df):
    
    
    df = clean_date_df.copy()
    
    # consider date as str : dd-mm-yyyy    
    df[DATE_OF_BIRTH] = df[DATE_OF_BIRTH].astype(str)
    
    df.insert(loc=0, column='jour', value='N/A')
    df.insert(loc=0, column='mois', value='N/A')
    df.insert(loc=0, column='annee', value='N/A')
    
    df['jour'] = df[DATE_OF_BIRTH].str[:2]
    df['mois'] = df[DATE_OF_BIRTH].str[3:-5]
    df['annee'] = df[DATE_OF_BIRTH].str[6:]

    df[DATE_OF_BIRTH] = df['annee']+ "-" + df['mois']+ "-" + df['jour']
    # clean invalide date
    df[DATE_OF_BIRTH] = df[DATE_OF_BIRTH].replace(['--na', '--N/','--'], 'N/A', regex=True)
    
    df = df.drop(['jour', 'mois', 'annee'], axis=1)
    
    
    clean_date_done = df[DATE_OF_BIRTH]
    return clean_date_done