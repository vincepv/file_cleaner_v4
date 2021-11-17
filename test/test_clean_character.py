import pandas as pd

from module.clean_fr.clean_gender_fr import clean_gender_fr

df_start = pd.DataFrame({'a': [Monsieur, Madame], 'b': [a, b]})

df = clean_gender_fr(df_start)

df_expect = pd.DataFrame({'a': [2, 1], 'b': [a, b]})



assert_frame_equal(df, df_expect)