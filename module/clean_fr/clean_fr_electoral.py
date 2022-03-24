import pandas as pd
from config import my_pandas_folder

from module.list.rename_column import rename_column

from module.clean_fr.clean_fr_file.clean_date_fr import clean_date_fr
from module.clean_fr.clean_fr_file.clean_gender_fr import clean_gender_fr
from module.clean_fr.clean_fr_file.clean_zip_fr import clean_zip_fr
from module.clean_fr.clean_fr_file.clean_mobile_fr import clean_mobile_fr

from module.clean_fr.clean_fr_electoral.clean_name import clean_name_electoral
from module.clean_fr.clean_fr_electoral.clean_electoral_col import clean_electoral_col
from module.clean_fr.clean_fr_electoral.create_adress2 import create_adresse2_electoral
from module.clean_fr.clean_fr_electoral.clean_adress import clean_adress_electoral
from module.clean_fr.clean_fr_electoral.create_keyword import create_keyword_electoral

def clean_electoral_fr(my_file_to_clean):
    """
    clean electoral csv file

    utf8 delimitor ,

    column must be renamed:
    - categorie
    - note
    - mot clef
    - sex
    - prenom
    - nom
    - numero = numero de rue
    - rue = rue
    - numero bv = numero du bureau de vote
    - date = date de naissance format jj/mm/aaaa

    """

    df = pd.read_csv(my_file_to_clean, low_memory=False)
    
    # clean header column
    df = df.rename(columns=rename_column)
    df = clean_electoral_col(df) 
    
    # clean process
    df['Adresse 2 '] = create_adresse2_electoral(df)
    df[['prenom','autre prenom','nomUsage']] = clean_name_electoral(df)
    df['date'] = clean_date_fr(df)
    df['sexe'] = clean_gender_fr(df)
    df['cp'] = clean_zip_fr(df)
    df[['mobile', 'clean_phone','clean_mobile']] = clean_mobile_fr(df)
    df['adresse'] = clean_adress_electoral(df) 
    df['mot clef'] = create_keyword_electoral(df)
    
    # remove duplicate
    df = df.drop_duplicates(subset=['prenom', 'nomUsage', 'nomNaissance', 'date'],keep='first')
    
    df.to_csv(my_pandas_folder+"clean_electoral.csv", header=True, index=False, encoding="utf8")