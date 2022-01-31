import geopandas
from config import my_pandas_folder

# check your env and packages

def convert_shapefile_to_geojson (my_shapefile):
    
    shp_file = geopandas.read_file(my_shapefile)
    shp_file.to_file(my_pandas_folder+'draft.geojson', driver='GeoJSON')