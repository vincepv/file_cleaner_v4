import pandas as pd

def clean_gender_fr(clean_gender_df):
    
    
    df = clean_gender_df.copy()
    df['sexe'] = df['sexe'].fillna('0')
    df['sexe'] = df['sexe'].astype(str)
    df['sexe'] = df['sexe'].str.replace('\.0$', '', regex=True)
    df['sexe'] = df['sexe'].str.strip()
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
    
    df['sexe'] = df['sexe'].replace(man_list, '2')
    df['sexe'] = df['sexe'].replace(woman_list, '1')
    clean_gender_done = df['sexe']
    
    return clean_gender_done