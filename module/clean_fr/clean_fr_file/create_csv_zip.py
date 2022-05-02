import pandas as pd
from config import my_pandas_folder

def create_csv_zip_file(my_dataframe):
  """
  
  create a csv zip file 
  
  
  """

  #need to manage utf8 > latin1 conversion for special character
  # add a steep to convert utf8 > latin1

  filename = 'cleanFile'

  compression_options = dict(
    method='zip', 
    archive_name=f'{filename}.csv'
  )
  
  my_dataframe.to_csv(
    my_pandas_folder+f'{filename}.zip',
    header=True,
    index=False,
    encoding='latin1',
    compression=compression_options,
  )