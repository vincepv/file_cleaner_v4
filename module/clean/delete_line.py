import os
import pandas as pd

def delete_line (my_folder):
  # Chemin du folder contenant les fichiers Excel
  folder = my_folder

  # Parcourir tous les fichiers dans le folder
  for file in os.listdir(folder):
      if file.endswith('.xlsx') or file.endswith('.xls'):
          file_path = os.path.join(folder, file)
          
          # Charger le file Excel en utilisant pandas
          df = pd.read_excel(file_path)
          
          # Récupérer la première ligne comme noms de colonne
          column_name = df.iloc[5].tolist()
          
          # Supprimer les 6 premières lignes
          df = df.iloc[6:]

          df.columns = column_name
          
          # Enregistrer les modifications dans le même file
          df.to_excel(file_path, index=False)
          