import pandas as pd
from config import my_pandas_folder

def clean_usa_date(my_file):
    
    df = pd.read_csv(my_file, low_memory=False)

    # replace invalid dates with NaN
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # drop rows with NaN dates
    df = df.dropna(subset=['date'])

    # convert dates to dd/mm/yyyy format
    df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

    df.to_csv(my_pandas_folder+"clean_usa_date.csv",header=True,index=False,encoding="utf8",sep=',')
