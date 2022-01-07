import pandas as pd
from config import *


def merge_on_city(input1,input2):
    """
    

    """
    # input1 = electoral file
    df1 = pd.read_csv(input1, low_memory=False)
    df2 = pd.read_csv(input2, low_memory=False)

    key = 'ville'
    # clean file for merge, case sensitive
    
    #df1
    df1[key] = df1[key].str.strip()
    df1[key] = df1[key].str.capitalize()
    
    #df2
    df2[key] = df2[key].str.strip()
    df2[key] = df2[key].str.capitalize()

    
    # create duplicate file to tracks duplicate contact not in merge file

    dfdup1 = df1[df1.duplicated([key], keep=False)]
    dfdup2 = df2[df2.duplicated([key], keep=False)]
    
    dfdup1.to_csv(my_pandas_folder+'/Duplicate1.csv', encoding='utf8', index=False)
    dfdup2.to_csv(my_pandas_folder+'/Duplicate2.csv', encoding='utf8', index=False)
    
    # remove duplicate before merge, avoid to merge false data

    df1 = df1.drop_duplicates(subset=[key],keep=False)
    df2 = df2.drop_duplicates(subset=[key],keep=False)
    
    df = pd.merge(df1, df2, on=[key], how='outer', indicator='Source')

    df.to_csv(my_pandas_folder+'MergeCity.csv', encoding='utf8', index=False)