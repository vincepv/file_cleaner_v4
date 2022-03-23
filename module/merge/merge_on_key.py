import pandas as pd
from config import my_pandas_folder


def merge_on_key(input1,input2):
    """
    key is used to merge 2 dataframe

    """

    df1 = pd.read_csv(input1, low_memory=False)
    df2 = pd.read_csv(input2, low_memory=False)

    # key is used to merge 2 files
    # bug when key is int
    key = ['nom','prenom']
    
    # clean file for merge, because case sensitive
    # remove space and uppercase 
    df1[key] = df1[key].apply(lambda x: x.str.strip())
    df1[key] = df1[key].apply(lambda x: x.str.capitalize())

    df2[key] = df2[key].apply(lambda x: x.str.strip())
    df2[key] = df2[key].apply(lambda x: x.str.capitalize())

    # create duplicate file to tracks duplicate contact not in merge file
    df1_duplicate = df1[df1.duplicated(subset=key, keep=False)]
    df2_duplicate = df2[df2.duplicated(subset=key, keep=False)]
    
    df1_duplicate.to_csv(my_pandas_folder+'/Duplicate1.csv', encoding='utf8', index=False)
    df2_duplicate.to_csv(my_pandas_folder+'/Duplicate2.csv', encoding='utf8', index=False)
    
    # remove duplicate before merge, avoid to merge false data
    df1 = df1.drop_duplicates(subset=key, keep=False)
    df2 = df2.drop_duplicates(subset=key, keep=False)
    
    df = pd.merge(df1, df2, on=key, how='outer', indicator='match status')

    # add duplicate 1 at the end of merge. 
    frames = [df, df1_duplicate]
    df = pd.concat(frames, sort=False)

    df.to_csv(my_pandas_folder+'mergeOnKey.csv', encoding='utf8', index=False)