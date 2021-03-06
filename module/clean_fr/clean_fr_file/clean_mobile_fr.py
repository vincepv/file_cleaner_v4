import pandas as pd
from config import MOBILE

def clean_mobile_fr(clean_mobile_df):
    
    
    df = clean_mobile_df.copy()
    df[MOBILE] = df[MOBILE].astype(str)
    
    dic_mobile_character = {
        '\.0$': '', 
        ' ': '', 
        '\.': '',
        '\-': '',
        '\_': '',
        '\(': '',
        '\)': '',
        '\,': '', 
        'nan': '',
        '/':''
    }
    
    dic_mobile_number = {
        '^06': '+336',
        '^07': '+337',
        '^6': '+336',
        '^7': '+337'
    }
    
    df[MOBILE] = df[MOBILE].replace(dic_mobile_character, regex=True)
    df[MOBILE] = df[MOBILE].replace(dic_mobile_number, regex=True)
    df.loc[df[MOBILE].duplicated(), [MOBILE]] = ''
    
        
    
    #extract mobile
    df.insert(loc=0, column='clean_mobile', value='N/A')
    df['clean_mobile'] = df[MOBILE].str.findall('^\+33\d{9}')
    df['clean_mobile'] = df['clean_mobile'].astype(str)
    dic_clean_mobile = {'\[': '', '\]': '', '\'': ''}
    df['clean_mobile'] = df['clean_mobile'].replace(dic_clean_mobile, regex=True)
    df.loc[df['clean_mobile'].duplicated(), ['clean_mobile']] = ''
    
    # extract phone
    df.insert(loc=0, column='clean_phone', value='N/A')
    df['clean_phone'] = df[MOBILE].str.findall('^0.+|^1.+|^2.+|^3.+|^4.+|^5.+|^8.+|^9.+')
    df['clean_phone'] = df['clean_phone'].astype(str)
    df['clean_phone'] = df['clean_phone'].replace(dic_clean_mobile, regex=True)
    df.loc[df['clean_phone'].duplicated(), ['clean_phone']] = ''
    
    
    clean_mobile_done = df[[MOBILE, 'clean_phone','clean_mobile']]
    
    return clean_mobile_done