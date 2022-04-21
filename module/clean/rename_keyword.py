import pandas as pd
from config import my_pandas_folder
from module.list.dic_rename_keyword import dic_rename_keyword

def rename_keyword(my_file):
    
    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")
    
    df['new key'] =  df['old key'].replace(dic_rename_keyword, regex=True)

    
    dic_key = {
        ",,,,":",",
        ",,,":",",
        ",,":",",
        "^\,":"",
        ",$":"",
        " ,":",",
        ", ":","
    }
    # clean keyword
    df['new key'] =  df['new key'].replace(dic_key, regex=True)
    
    df.to_csv(my_pandas_folder+'rename_keyword.csv', header=True, index=False, encoding="utf8")