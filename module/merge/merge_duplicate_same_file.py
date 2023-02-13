import pandas as pd
from config import my_pandas_folder

# https://www.skytowner.com/explore/merging_rows_within_a_group_together_in_pandas

def merge_duplicate_same_file(input1):
    """
      find inside 1 file duplicate row based on key
      then merge duplicate in 1 row 
      keep non-duplicate row in the clean file

    """
    # read file
    # key is used to merge 
    # aggregation_parameter indicates which columns needed for the clean file
    df = pd.read_csv(input1, low_memory=False)
    key = ['prenom','nom']
    aggregation_parameter = { 
      'Keywords' : ','.join,
      'Gender': 'first', 
      'Date of Birth': 'first',
      'Mobile': 'first',
      'Email': 'first',
      'Category': 'first',
      'Zip': 'first',
      'Street Address': 'first', 
      'City': 'first',
      'Profession': 'first',	
      'Organisme': 'first',	
      'Adresse 2': 'first',	
      'Formule': 'first',	
      'Tel Fixe': 'first',
      'Mobile 2': 'first',	
      'Accord': 'first',	
      'Appel': 'first',
      'Mandat2': 'first',
      'Mandat': 'first',	
      'Nom De Naissance': 'first',	
      'Intitule': 'first',	
      'Email2': 'first'
      }
    df[key] = df[key].astype(str)

    # clean file for merge, because case sensitive
    # remove space and uppercase 
    df[key] = df[key].apply(lambda x: x.str.strip())
    df[key] = df[key].apply(lambda x: x.str.capitalize())
    
    # find duplicate , remove it
    df_duplicate = df[df.duplicated(subset=key, keep=False)]
    df = df.drop_duplicates(subset=key, keep=False)
    
    # merge duplicate on key
    df_duplicate = df_duplicate.groupby(by= key, as_index=False).agg(aggregation_parameter)
    
    # append duplicate to non-duplicate
    frames = [df_duplicate, df]
    df = pd.concat(frames, sort=False)

    # clean character 
    df = df.astype(str)
    df = df.replace('\.0', '', regex=True)
    df = df.replace('nan', '', regex=True)
    df = df.replace('None', '', regex=True)

    # create file
    df.to_csv(my_pandas_folder+'merge_duplicate_same_file.csv', encoding='utf8', index=False)