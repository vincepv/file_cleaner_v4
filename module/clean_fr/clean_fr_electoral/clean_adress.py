import pandas as pd

from config import NUMBER ,STREET , ADDRESS

def clean_adress_electoral (my_dataframe):
    df = my_dataframe.copy()
    
    # Need to fix : if address column already exist, it delete address
    
    df[NUMBER] = df[NUMBER].astype(str)
    df[STREET] = df[STREET].astype(str)
    df[ADDRESS] = df[NUMBER]+' '+df[STREET]

    # clean part
    df[ADDRESS] = df[ADDRESS].str.replace(',', '', regex=True)
    df[ADDRESS] = df[ADDRESS].str.replace('^ ', '', regex=True)
    df[ADDRESS] = df[ADDRESS].str.replace(' $', '', regex=True)
    df[ADDRESS] = df[ADDRESS].str.replace('nan', '', regex=True)
    df[ADDRESS] = df[ADDRESS].str.replace('N/A N/A', 'N/A', regex=True)

    return df[ADDRESS]