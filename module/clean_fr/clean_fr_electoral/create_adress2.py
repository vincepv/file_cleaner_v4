import pandas as pd


def create_adresse2_electoral(my_dataframe):

    df = my_dataframe.copy()
    if 'complément 1' and 'complément 2' and 'lieu-dit' in df:
        df['adresse2'] = df['complément 1'].map(str) + " " +df['complément 2'].map(str) + " " +df['lieu-dit'].map(str)
        df['adresse2'] = df['adresse2'].str.replace('nan', '', regex=True)
        df['adresse2'] = df['adresse2'].str.strip()
        return df['adresse2']
    