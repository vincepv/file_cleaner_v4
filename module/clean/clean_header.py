import glob
import os
import pandas as pd

from config import my_pandas_folder


def clean_header(folder_to_clean):
    
    # get all csv files inside the folder
    all_files = glob.glob(folder_to_clean + "/*.csv")
    
    for file_path  in all_files:
        
    
        df = pd.read_csv(file_path, index_col=None, header=0, sep=',', low_memory=False)
        
        df.columns = df.columns.str.strip()
        df.columns = df.columns.str.lower()
        
        file_name = os.path.basename(file_path)
        df.to_csv(my_pandas_folder+file_name, encoding= 'utf8', index=False)
        
    
