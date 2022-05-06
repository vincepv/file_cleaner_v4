import pandas as pd

from config import *

from module.clean_fr.clean_fr_file.clean_column_fr import clean_column_fr
from module.clean_fr.clean_fr_file.clean_email_fr import clean_email_fr
from module.clean_fr.clean_fr_file.clean_gender_fr import clean_gender_fr
from module.clean_fr.clean_fr_file.clean_address_fr import clean_address_fr
from module.clean_fr.clean_fr_file.clean_keyword_fr import clean_keyword_fr
from module.clean_fr.clean_fr_file.clean_zip_fr import clean_zip_fr
from module.clean_fr.clean_fr_file.clean_mobile_fr import clean_mobile_fr
from module.clean_fr.clean_fr_file.clean_empty_name_fr import clean_empty_name_fr

def clean_file_fr(my_file):
    """ 
    clean csv file
    column must be renamed according to config file
    
    """

    df = pd.read_csv(
        my_file,
        low_memory=False, 
        sep=",",
        encoding="utf-8",
        parse_dates=[DATE_OF_BIRTH],
        )
    
    # clean column
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()
    df = clean_column_fr(df)
    
    # clean process
    df[[LAST_NAME,FIRST_NAME]] =  clean_empty_name_fr(df)
    df[EMAIL] = clean_email_fr(df)
    df[GENDER] = clean_gender_fr(df)
    df[ADDRESS] = clean_address_fr(df)
    df[ZIP] = clean_zip_fr(df)
    df[[MOBILE, 'phone_clean','mobile_clean']] = clean_mobile_fr(df)
    df[KEYWORD] = clean_keyword_fr(df)
    df = df.drop_duplicates()
    
    df.to_csv(my_pandas_folder+'cleanFile.csv',header=True,index=False,encoding='utf8',)
