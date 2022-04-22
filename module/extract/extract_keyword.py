import pandas as pd
from config import my_pandas_folder

def extract_keyword(my_file):
    """
  
    """
    df = pd.read_csv(my_file, low_memory=False)
    df_keyword = df['mot clef']
    df_keyword = df_keyword.str.split(pat=",", n=- 1, expand=True)

    # select column in df_keyword to concact

    number_column = len(df_keyword.columns)
    
    column_to_concat = []
    while number_column > 0:
        column_to_concat.append(df_keyword[number_column-1])
        number_column -= 1
    
    
    #merge all columns in 1 big column
    df_count = pd.concat(column_to_concat, axis=0)
    
    
    # count occurence, reset index avoid column name drop
    df_excel = df_count.value_counts().reset_index()
    df_excel.columns=['keyword', 'count']
    df_excel.to_excel(my_pandas_folder+'/keyword.xlsx', header=True, index=False, encoding="utf8")