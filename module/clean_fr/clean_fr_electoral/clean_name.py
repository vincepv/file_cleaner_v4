import pandas as pd


def clean_name_electoral(my_dataframe):
    df = my_dataframe.copy()

    df[['prenom','autre prenom']] = df['prenom'].str.split(' ',n=1, expand=True)
    df['prenom'] = df['prenom'].str.capitalize()
    df['nomUsage'] = df['nomUsage'].fillna(df['nomNaissance'])

    return df[[
        'prenom',
        'autre prenom',
        'nomUsage'
    ]]