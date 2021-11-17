import pandas as pd

from config import *


def keyword_add_to_column(my_file):
    """
    
    in keywords column, extract specific value
    put specific value in a specific column
    
    """

    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")
    # warning ! must escape regex /  ' ( ) in pattern
    pat_fonction = '(AA|BBB|CC)'
    pat_organisme = '(ZZZ|TTT|UUU)'
    pat_profession = '(AGRICULTEUR|Artisan-e|CSP SANTE)'
    
    
    df['generat_fonction'] = df['old mot clef'].str.extract(pat = pat_fonction )
    df['generat_organisme'] = df['old mot clef'].str.extract(pat = pat_organisme )
    df['generat_profession'] = df['old mot clef'].str.extract(pat = pat_profession )
    
    df.to_csv(my_pandas_folder+'add_keyword_to_column.csv', header=True, index=False, encoding="utf8")