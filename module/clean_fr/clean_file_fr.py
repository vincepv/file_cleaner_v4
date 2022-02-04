import pandas as pd

from config import my_pandas_folder

from module.clean_fr.clean_fr_file.clean_column_fr import clean_column_fr
from module.clean_fr.clean_fr_file.clean_email_fr import clean_email_fr
from module.clean_fr.clean_fr_file.clean_date_fr import clean_date_fr
from module.clean_fr.clean_fr_file.clean_gender_fr import clean_gender_fr
from module.clean_fr.clean_fr_file.clean_address_fr import clean_address_fr
from module.clean_fr.clean_fr_file.clean_zip_fr import clean_zip_fr
from module.clean_fr.clean_fr_file.clean_mobile_fr import clean_mobile_fr
from module.clean_fr.clean_fr_file.clean_empty_name_fr import clean_empty_name_fr

def clean_file_fr(my_file):
    """ 
    clean csv file

    column must be renamed
    'prenom' 
    'nom' 
    'sexe' 
    'adresse'
    'cp' 
    'ville'
    'date' format dd/m/yyyy
    'note'
    'mot clef'
    'email'
    'mobile' 
    
    """

    df = pd.read_csv(my_file, low_memory=False, sep=",",encoding="utf-8")
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.strip()

    df = clean_column_fr(df)
    df =  clean_empty_name_fr(df)
    df['email'] = clean_email_fr(df)
    df['date'] = clean_date_fr(df)
    df['sexe'] = clean_gender_fr(df)
    df['adresse'] = clean_address_fr(df)
    df['cp'] = clean_zip_fr(df)
    df[['mobile', 'phone_clean','mobile_clean']] = clean_mobile_fr(df)
    df = df.drop_duplicates()
    
    df.to_csv(my_pandas_folder+"DraftClean.csv", header=True, index=False, encoding="utf8")