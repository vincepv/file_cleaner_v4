import pandas as pd
from config import my_pandas_folder


def merge_duplicate(input):
    """
    merge duplicates contact in 1 line
    maybe lead to messy data after merge

    """

    df = pd.read_csv(input, low_memory=False)
    
    # find duplicate
    # key = ['prenom','nom','cp'] or key = ['prenom']
    key = ['First Name','Last Name', 'Street Address']
    df[key] = df[key].astype(str)
    df_duplicate = df[df.duplicated(subset=key, keep=False)]
    
    #clean duplicate
    df_duplicate_clean = df_duplicate.groupby('value')['tempx'].apply(' '.join).reset_index()

    df_duplicate_clean.to_csv(my_pandas_folder+'/Duplicate.csv', encoding='utf8', index=False)
    
    # merge clean duplicate and database
    df = df.drop_duplicates(subset=key, keep=False)
    frames = [df, df_duplicate_clean]
    df = pd.concat(frames, sort=False)
 
    # clean ending .0 
    df = df.astype(str)
    df = df.replace('\.0', '', regex=True)
    df = df.replace('nan', '', regex=True)

    df.to_csv(my_pandas_folder+'mergeDuplicate.csv', encoding='utf8', index=False)