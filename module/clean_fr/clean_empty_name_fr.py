import pandas as pd

def clean_empty_name_fr(clean_empty_name_column):
    
    """
    Fill empty firstname and lastname with organisation
    """
    
    df = clean_empty_name_column.copy()
    
    if 'organisme' in df:
        df['nom'] = df['nom'].fillna(df['organisme'])
        df['prenom'] = df['prenom'].fillna(df['organisme'])

    dic_organisme_clean = {
        '\'':' ',
        '^ ':'',
        '\d': '',
        '\.': '',
        '&': 'et',
        '\(':'',
        '\)':'',
        '-':'',
        'à':'',
        '/':' ',
        ',':'',
        '(?<=^.{45}).+':'',
    }
    
    df[['nom','prenom']] = df[['nom','prenom']].replace(dic_organisme_clean, regex=True)
    clean_empty_name_done  = df
    return clean_empty_name_done