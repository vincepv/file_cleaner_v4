import pandas as pd

def clean_column_fr(clean_column_df):
    
    df = clean_column_df.copy()
    
    if 'prenom' not in df:
        df.insert(loc=0, column='prenom', value='')

    if 'nom' not in df:
        df.insert(loc=0, column='nom', value='')

    if 'sexe' not in df:
        df.insert(loc=0, column='sexe', value='0')

    if 'date' not in df:
        df.insert(loc=0, column='date', value='')

    if 'mobile' not in df:
        df.insert(loc=0, column='mobile', value='')

    if 'adresse' not in df:
        df.insert(loc=0, column='adresse', value='')
    
    if 'ville' not in df:
        df.insert(loc=0, column='ville', value='')

    if 'cp' not in df:
        df.insert(loc=0, column='cp', value='')
    
    if 'pays' not in df:
        df.insert(loc=0, column='pays', value='FR')
    else:
        df['pays'] = df['pays'].astype(str)
        df['pays'] = df['pays'].replace(['FRANCE','france','France'],'FR')
        df['pays'] = df['pays'].replace(['nan'],'N/A')

    if 'categorie' not in df:
        df.insert(loc=0, column='categorie', value='2')
    if 'note' not in df:
        df.insert(loc=0, column='note', value='')
    if 'mot clef' not in df:
        df.insert(loc=0, column='mot clef', value='')
    else:
        df['mot clef'] = df['mot clef'].str.strip(to_strip=",")
        
    if 'email' not in df:
        df.insert(loc=0, column='email', value='')
        
    clean_column_done  = df

    return clean_column_done