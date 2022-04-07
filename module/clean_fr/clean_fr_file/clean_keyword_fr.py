import pandas as pd


def clean_keyword_fr(clean_keyword_df):
    

    df = clean_keyword_df.copy()
    df['mot clef'] = df['mot clef'].fillna('')
    df['mot clef'] = df['mot clef'].astype(str)
    df['mot clef'] = df['mot clef'].str.replace('\.0$', '', regex=True)
    df['mot clef'] = df['mot clef'].str.upper()

    clean_delimitor = [
        ";",
        " ;",
        "; ",
        " ; ",
        " ,",
        ", ",
        " , "
    ]
    df['mot clef'] = df['mot clef'].replace(clean_delimitor, ',', regex=True)
    

    clean_leading_trailing =[
        "^,",
        ",$",
        "^;",
        ";$"
    ]
    df['mot clef'] = df['mot clef'].replace(clean_leading_trailing, '', regex=True)

    clean_keyword_done = df['mot clef']

    return clean_keyword_done