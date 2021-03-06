import pandas as pd
import glob
from config import my_pandas_folder


def merge_csv(folder_csv): 
    """
    
    merge a folder with utf8 csv in one master csv file
    
    """
    all_files = glob.glob(folder_csv + "/*.csv")
    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0, sep=';', low_memory=False)
        li.append(df)
    df = pd.concat(li, axis=0, ignore_index=True, sort=True)
    df.to_csv(my_pandas_folder+'DraftCsvMerge.csv', encoding= 'utf8', index=False)
    