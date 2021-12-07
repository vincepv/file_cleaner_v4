import pandas as pd
from config import my_pandas_folder

from module.list.rename_column import rename_column
from module.clean_fr.clean_date_fr import clean_date_fr
from module.clean_fr.clean_gender_fr import clean_gender_fr
from module.clean_fr.clean_zip_fr import clean_zip_fr
from module.clean_fr.clean_mobile_fr import clean_mobile_fr

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
    df = df.rename(columns=rename_column)
    # check columns in csv
    if 'categorie' not in df:
        df.insert(loc=0, column='categorie', value='3')
    if 'note' not in df:
        df.insert(loc=0, column='note', value='')
    if 'mot clef' not in df:
        df.insert(loc=0, column='mot clef', value='')
    if 'sexe' not in df:
        df.insert(loc=0, column='sexe', value='0')
    if 'prenom' not in df:
        df.insert(loc=0, column='prenom', value='prenom a renseigner')
    else:
        df['prenom'] = df['prenom'].fillna('A')
    if 'pays' not in df:
        df.insert(loc=0, column='pays', value='FR')
    else:
        df['pays'] = df['pays'].astype(str)
        df['pays'] = df['pays'].replace(['FRANCE', 'france', 'France'], 'FR')
        df['pays'] = df['pays'].replace(['nan'], 'N/A')
    if 'ville' not in df:
        df.insert(loc=0, column='ville', value='N/A')
    if 'cp' not in df:
        df.insert(loc=0, column='cp', value='N/A')
    if 'adresse' not in df:
        df.insert(loc=0, column='adresse', value='N/A')
    if 'rue' not in df:
        df.insert(loc=0, column='rue', value='N/A')
    if 'numero' not in df:
        df.insert(loc=0, column='numero', value='N/A')
    if 'date' not in df:
        df.insert(loc=0, column='date', value='N/A')
    if 'mobile' not in df:
        df.insert(loc=0, column='mobile', value='')
    else:
        df['mobile'] = df['mobile'].fillna('')

    if 'email' not in df:
        df.insert(loc=0, column='email', value='N/A')
    else:
        df['email'] = df['email'].fillna('N/A')
        
    #create address 2
    
    if 'complément 1' and 'complément 2' and 'lieu-dit' in df:
        df['adresse2'] = df['complément 1'].map(str) + " " +df['complément 2'].map(str) + " " +df['lieu-dit'].map(str)
        df['adresse2'] = df['adresse2'].str.replace('nan', '', regex=True)
        df['adresse2'] = df['adresse2'].str.strip()

    # keep begining of first name
    df[['prenom','autre prenom']] = df['prenom'].str.split(' ',n=1, expand=True)
    df['prenom'] = df['prenom'].str.capitalize()
    df['nomUsage'] = df['nomUsage'].fillna(df['nomNaissance'])

    
    df['date'] = clean_date_fr(df)
    df['sexe'] = clean_gender_fr(df)
    df['cp'] = clean_zip_fr(df)
    df[['mobile', 'clean_phone','clean_mobile']] = clean_mobile_fr(df)

    # clean address . Need to fix : if address column already exist, it delete address

    df['numero'] = df['numero'].astype(str)
    df['rue'] = df['rue'].astype(str)
    df['adresse'] = df['numero']+' '+df['rue']

    df['adresse'] = df['adresse'].str.replace(',', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('^ ', '', regex=True)
    df['adresse'] = df['adresse'].str.replace(' $', '', regex=True)

    # renomme les cellules vides issues provenant de numeroe et rue
    df['adresse'] = df['adresse'].str.replace('nan', '', regex=True)
    df['adresse'] = df['adresse'].str.replace('N/A N/A', 'N/A', regex=True)


    # keyword
    if 'numero bv' in df:
        df['numero bv'] = df['numero bv'].astype(str)
        df['numero bv'] = df['numero bv'].str.replace('\.0$', '', regex=True)
        df['mot clef'] = df['mot clef']+',BV '+df['numero bv']


    df['mot clef'] = df['mot clef'].astype(str)
    df['mot clef'] = df['mot clef'].str.replace('\.0$', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('nan', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace('^,', '', regex=True)
    df['mot clef'] = df['mot clef'].str.replace(';', ',', regex=True)

    
    
    df = df.drop_duplicates(subset=['prenom', 'nomUsage', 'nomNaissance', 'date'],keep='first')
    
    df.to_csv(my_pandas_folder+"clean_electoral.csv", header=True, index=False, encoding="utf8")
    