import pandas as pd
from config import my_pandas_folder

def autofill(my_file) :
    
    
    df = pd.read_csv(my_file, low_memory=False)
    df['ville'] = df['ville'].ffill(axis=0)
    df.to_csv(my_pandas_folder+"autofill.csv", header=True, index=False, encoding="utf8")