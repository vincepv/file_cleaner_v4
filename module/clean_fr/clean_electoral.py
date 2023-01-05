import pandas as pd
from config import *

from module.list.rename_column import rename_column

from module.clean_fr.regulare_file.clean_gender_fr import clean_gender_fr
from module.clean_fr.regulare_file.clean_zip_fr import clean_zip_fr
from module.clean_fr.regulare_file.clean_mobile_fr import clean_mobile_fr

from module.clean_fr.electoral_file.clean_name import clean_name_electoral
from module.clean_fr.electoral_file.clean_electoral_col import clean_electoral_col
from module.clean_fr.electoral_file.create_adress2 import create_adresse2_electoral
from module.clean_fr.electoral_file.clean_address import clean_address_electoral
from module.clean_fr.electoral_file.create_keyword import create_keyword_electoral
from module.clean_fr.electoral_file.clean_date import clean_date


def clean_electoral_fr(my_file_to_clean):
    """
    clean electoral utf8 csv file
    column must be renamed according to config file
    must create a date of birth column

    """
    df = pd.read_csv(
        my_file_to_clean,
        low_memory=False,
        )
    
    # clean header column
    df = df.rename(columns=rename_column)
    df = clean_electoral_col(df) 
    
    # clean process
    df[ADDRESS_2] = create_adresse2_electoral(df)
    df[[FIRST_NAME,'other name',COMMON_NAME]] = clean_name_electoral(df)
    df[GENDER] = clean_gender_fr(df)
    df[ZIP] = clean_zip_fr(df)
    df[[MOBILE, 'clean_phone','clean_mobile']] = clean_mobile_fr(df)
    df[ADDRESS] = clean_address_electoral(df) 
    df[KEYWORD] = create_keyword_electoral(df)
    df[DATE_OF_BIRTH] = clean_date(df)

    # remove duplicate
    df = df.drop_duplicates(subset=[FIRST_NAME, COMMON_NAME, BIRTH_NAME, DATE_OF_BIRTH],keep='first')

    df.to_csv(
        my_pandas_folder+"clean_electoral.csv", 
        header=True, 
        index=False, 
        encoding="utf8",
        
        )
    
    