import pandas as pd
from config import my_pandas_folder

# https://www.skytowner.com/explore/merging_rows_within_a_group_together_in_pandas

def merge_duplicate_same_file(input1):
    """
   

    """
    # read file
    # key is used to merge 
    df = pd.read_csv(input1, low_memory=False)
    key = ['prenom','nom']
    df[key] = df[key].astype(str)

    # clean file for merge, because case sensitive
    # remove space and uppercase 
    df[key] = df[key].apply(lambda x: x.str.strip())
    df[key] = df[key].apply(lambda x: x.str.capitalize())
    
    # find duplicate , remove it
    df_duplicate = df[df.duplicated(subset=key, keep=False)]
    df = df.drop_duplicates(subset=key, keep=False)
    
    # merge duplicate on key
    df_duplicate = df_duplicate.groupby(by= key, as_index=False).agg({'nom' : 'first', 'Gender': 'first' , 'Category':'first' , 'Keywords' : ','.join })
    
   
    # append duplicate to non-duplicate
    frames = [df_duplicate, df]
    df = pd.concat(frames, sort=False)

    # # clean character 
    # df = df.astype(str)
    # df = df.replace('\.0', '', regex=True)
    # df = df.replace('nan', '', regex=True)

    # # create file
    df.to_csv(my_pandas_folder+'merge_duplicate_same_file.csv', encoding='utf8', index=False)