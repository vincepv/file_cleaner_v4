import pandas as pd
from config import my_pandas_folder


def keyword_add_to_column(my_file):
    """
    
    in [keywords] column, extract specific value
    then put specific value in a specific column
    
    """

    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")
    # warning ! must escape regex /  ' ( ) in pattern
    pattern_fonction = '(AA|BBB|CC)'
    pattern_organisme = '(ZZZ|TTT|UUU)'
    pattern_profession = '(AGRICULTEUR|Artisan-e|CSP SANTE)'
    
    
    df['generate_fonction'] = df['keywords'].str.extract(pat = pattern_fonction )
    df['generate_organisme'] = df['keywords'].str.extract(pat = pattern_organisme )
    df['generate_profession'] = df['keywords'].str.extract(pat = pattern_profession )
    
    df.to_csv(my_pandas_folder+'add_keyword_to_column.csv', header=True, index=False, encoding="utf8")