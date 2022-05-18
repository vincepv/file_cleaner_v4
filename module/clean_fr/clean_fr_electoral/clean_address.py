import pandas as pd

from config import NUMBER ,STREET , ADDRESS

def clean_address_electoral (my_dataframe):
    df = my_dataframe.copy()
    
    # Need to fix : if address column already exist, it delete address
    if ADDRESS not in df:
        df[NUMBER] = df[NUMBER].astype(str)
        df[STREET] = df[STREET].astype(str)
        df[[NUMBER,STREET]] = df[[NUMBER,STREET]].replace('nan', '')
        df[ADDRESS] = df[NUMBER]+' '+df[STREET]

        # clean part
        clean_character = {
            ',':'',
            '^ ':'',
            ' $':'',
            '/':' ',
            '_':' ',
            '\.0':'', 
        }

        df[ADDRESS] = df[ADDRESS].replace(clean_character, regex=True)
        return df[ADDRESS]
    else :
        return df[ADDRESS]