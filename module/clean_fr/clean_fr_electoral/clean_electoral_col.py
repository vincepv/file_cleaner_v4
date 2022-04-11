import pandas as pd


def clean_electoral_col(my_dataframe):
    
    df = my_dataframe.copy()

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

    return df