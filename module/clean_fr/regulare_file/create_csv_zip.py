import pandas as pd

from config import my_pandas_folder


def create_csv_zip_file(my_dataframe):
  """
  
  create a csv zip file 
  
  
  """

  #generate file latin1 csv zip

  filename = 'cleanFile'

  compression_options = dict(
    method='zip', 
    archive_name=f'{filename}.csv'
  )
  
  my_dataframe.to_csv(
    my_pandas_folder+f'{filename}.zip',
    header=True,
    index=False,
    encoding='utf8',
    compression=compression_options,
  )