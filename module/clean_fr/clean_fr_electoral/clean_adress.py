import pandas as pd

def clean_adress_electoral (my_dataframe):
    df = my_dataframe.copy()
    
    # Need to fix : if address column already exist, it delete address
    
    df['numero'] = df['numero'].astype(str)
    df['rue'] = df['rue'].astype(str)
    df['adresse'] = df['numero']+' '+df['rue']

    # clean part
    df['adresse'] = df['adresse'].str.replace(',', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('^ ', '', regex=True)
    df['adresse'] = df['adresse'].str.replace(' $', '', regex=True)

    
    df['adresse'] = df['adresse'].str.replace('nan', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('N/A N/A', 'N/A', regex=True)

    return df['adresse']