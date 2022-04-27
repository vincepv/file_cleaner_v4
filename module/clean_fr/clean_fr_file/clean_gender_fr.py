import pandas as pd
from config import GENDER

def clean_gender_fr(clean_gender_df):
    
    
    df = clean_gender_df.copy()
    df[GENDER] = df[GENDER].fillna('0')
    df[GENDER] = df[GENDER].astype(str)
    df[GENDER] = df[GENDER].str.replace('\.0$', '', regex=True)
    df[GENDER] = df[GENDER].str.strip()
    man_list = [
        'monsieur', 
        'Monsieur', 
        'MONSIEUR', 
        'Mr',
        'MR', 
        'M.',
        'M',
        'mr',
        'm',
        'Masculin',
        'H',
        'Homme'
    ]
    woman_list = [
        'madame', 
        'Madame', 
        'MADAME', 
        'Ms', 
        'MS', 
        'Mme', 
        'MME', 
        'Mlle', 
        'MLLE',
        'mlle', 
        'Mme', 
        'F', 
        'mme',
        'Féminin',
        'Femme'
    ]
    
    df[GENDER] = df[GENDER].replace(man_list, '2')
    df[GENDER] = df[GENDER].replace(woman_list, '1')
    clean_gender_done = df[GENDER]
    
    return clean_gender_done