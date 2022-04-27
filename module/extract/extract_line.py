import pandas as pd
from config import my_pandas_folder

def extract_line(my_file,column_name,value_to_extract):
    """
    my_file: name of the file to process
    column_name: name of the column where extract is process
    value_to_extract: value to use for extract in the given column

    >return a new file with only lines matching param
    Example 1. with 2 param
    
    
    df_extract = df.loc[(df[column_name] == value_to_extract) & (df[column_name_2] == value_to_extract_2) ]
    
    Going further :  with 'or' logic, extract base on 2 conditions
    condition_to_extract = (df['nombre'] > 200) | (df['result'] > 30)
    df_extract = df.loc[condition_to_extract]
    
    
    """
    df = pd.read_csv(my_file, low_memory=False)
    df_extract = df.loc[(df[column_name] == value_to_extract)]
    df_extract.to_csv(my_pandas_folder+'extract.csv', header=True, index=False, encoding="utf8")