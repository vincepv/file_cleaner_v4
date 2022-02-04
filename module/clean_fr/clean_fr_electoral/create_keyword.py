import pandas as pd

def create_keyword_electoral (my_dataframe):
    df = my_dataframe.copy()

    if 'numero bv' in df:
        df['numero bv'] = df['numero bv'].astype(str)
        df['numero bv'] = df['numero bv'].str.replace('\.0$', '', regex=True)
        df['mot clef'] = df['mot clef']+',BV '+df['numero bv']


    df['mot clef'] = df['mot clef'].astype(str)
    df['mot clef'] = df['mot clef'].str.replace('\.0$', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('nan', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('^,', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace(';', ',', regex=True)

    return df['mot clef']