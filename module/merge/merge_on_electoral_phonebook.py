import pandas as pd
from config import *
 
def merge_on_electoral_phonebook (electoral_list,phone_book):


    """
    csv file in utf8
    electoral_list is the electoral list csv
    phone_book is the mobile or email csv to merge with electoral_list
    """

    df_electoral = pd.read_csv(electoral_list, low_memory=False)
    df_phonebook = pd.read_csv(phone_book, low_memory=False)

    # avoid case sensitive issue. Marc and MARC is different during merge process
  
    df_electoral['prenom'] = df_electoral['prenom'].str.strip()
    df_electoral['nom'] = df_electoral['nom'].str.strip()
    df_electoral['prenom'] = df_electoral['prenom'].str.capitalize()
    df_electoral['nom'] = df_electoral['nom'].str.capitalize()

    df_phonebook['prenom'] = df_phonebook['prenom'].str.strip()
    df_phonebook['nom'] = df_phonebook['nom'].str.strip()
    df_phonebook['prenom'] = df_phonebook['prenom'].str.capitalize()
    df_phonebook['nom']= df_phonebook['nom'].str.capitalize()

    
    # create duplicate file to tracks duplicate contact not in merge file

    df_dup_electoral = df_electoral[df_electoral.duplicated(['prenom', 'nom'], keep=False)]
    df_dup_phonebook = df_phonebook[df_phonebook.duplicated(['prenom', 'nom'], keep=False)]
    
    df_dup_electoral.to_csv(my_pandas_folder+'/DuplicateElectoral.csv', encoding='utf8', index=False)
    df_dup_phonebook.to_csv(my_pandas_folder+'/DuplicatePhoneBookOnly.csv', encoding='utf8', index=False)
    
    # remove duplicate before merge, to avoid merge data to wrong contact

    df_electoral = df_electoral.drop_duplicates(subset=['prenom', 'nom'],keep=False)
    df_phonebook = df_phonebook.drop_duplicates(subset=['prenom', 'nom'],keep=False)
    
    df_merge = pd.merge(df_electoral, df_phonebook, on=['prenom', 'nom'], how='right', indicator='Source')
    
    # add duplicate phonebook to dataframe to avoid losing phonebook data.
    frames = [df_merge, df_dup_phonebook]
    df = pd.concat(frames, sort=False)
    
    # clean ".O" string
    column = ['mobile','sexe','cp','categorie']
    df[column] = df[column].astype(str)
    df[column] = df[column].replace('\.0', '', regex=True)
    df[column] = df[column].replace('nan', '', regex=True)
    
    df.to_csv(my_pandas_folder+'MergePhoneBookWithDuplicate.csv', encoding='utf8', index=False)