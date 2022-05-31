import pandas as pd
from config import my_pandas_folder

def clean_character(file_to_clean):
    
	df = pd.read_csv(file_to_clean, low_memory=False)

	clean_dict = {
		'Ã©' : 'é',
		'Ã¨' : 'è',
		'Ã«' : 'ë',
		'Ã§' : 'ç',
		'Ã®' : 'î',
		'Ã‰' : 'E',
		'Ã”' : 'O',
		'Ã¢' : 'â',
		'Ã¯' : 'ï',
		'Ã´' : 'ô',
		'Ãª' : 'ê',
		'Ãˆ' : 'E',
		'Ο©':'é',
		'Οß':'c',
		'ΟΪ':'e',
		'Ο®':'è',
		'Ο¥':'o',
		'Ο°':'i',
		'Ο·':'i',

	}

	df = df.replace(clean_dict, regex=True)

	df.to_csv(my_pandas_folder+"clean_character.csv", encoding= 'utf8', index=False)