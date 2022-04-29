import pandas as pd
from config import my_pandas_folder

def create_zip_csv_file(my_dataframe):
  """
  
  create a csv zip file 
  encoding latin1
  
  """

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