import pandas as pd
from config import my_pandas_folder

def sort_address(my_file):

    df = pd.read_csv(my_file)

    # extract number and address in 2 columns
    df['street'] = df['adresse'].str.split(pat="\d")
    df['number'] = df['adresse'].str.split(pat="\D")

    # columns cleaning
    df['street'] = df['street'].astype(str)
    df['number'] = df['number'].astype(str)

    list= ["-",",","\[","\]","\'","\"","     ","    ","   ","  "]
    
    df['number'] = df['number'].replace(list,'',regex=True)
    df['street'] = df['street'].replace(list,'',regex=True)

    #change street to int for sorting 
    df['number'] = pd.to_numeric(df['number'],errors='coerce')
    df = df.sort_values(by=['street','number'])
    # False result : when sort 2A, 2B, 3C, Bis, ter address.
    
    df.to_csv(my_pandas_folder+"/address_sort.csv",header=True,index=False,encoding="utf8")

