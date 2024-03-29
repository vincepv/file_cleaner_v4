import pandas as pd
import glob
from config import *


def merge_excel(excel_folder):
    """
    convert excel folder in one master utf8 csv file

    """
    
    all_files = glob.glob(excel_folder + "/*.xls")
    li = []
    for filename in all_files:
        df = pd.read_excel(filename, index_col=None, header=0)
        li.append(df)
    df = pd.concat(li, axis=0, ignore_index=False, sort=True)
    df.to_csv(my_pandas_folder+'excel_merge.csv', encoding= 'utf8', index=False, )