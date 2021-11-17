import pandas as pd
from config import my_pandas_folder
from module.list.country_dict import country_dict 

def clean_country(my_file):
    
    
    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")
    df['pays'] = df['pays'].replace(country_dict, regex=True)

    df.to_csv(my_pandas_folder+"clean_country.csv", header=True, index=False, encoding="utf8")