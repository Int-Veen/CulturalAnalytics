import pandas as pd
import shutil
import os
import seaborn as sns
import matplotlib.pyplot as plt

# Pfad zur CSV Datei
file_path = '../data/wikiart_art_pieces.csv'
d = {}

# CSV-Datei einlesen
df = pd.read_csv(file_path)
# Zählen, wie oft "nude painting (nu)" in der Spalte "genre" vorkommt
for g in df["genre"]:
    for x in g.split(","):
        d[x] = True

# Filtern der Daten, um nur die Zeilen mit "nude painting (nu)"
df_nude = df[df['genre'].str.contains('nude painting', case=False, na=False)]

# Erstellen einer neuen CSV-Datei mit den gefilterten Daten
df_nude.to_csv('../data/filtered_genres_nude_painting.csv', index=False)

print("Die gefilterte Datei wurde erstellt und als 'filtered_genres_nude_painting.csv' gespeichert.")

# KOPIEREN DER BILDER VON NUDE PAINTING

# Pfad zum Quellordner, wo sich alle Bilder befinden
source_folder = '../data/wikiart'

# Pfad zum Zielordner, in den die gefilterten Bilder kopiert werden sollen
destination_folder = '../data/zielordner_nude_painting'


# Kopieren der Bilder
for file_name in df_nude['file_name']:
    source_file = os.path.join(source_folder, file_name)
    destination_file = os.path.join(destination_folder, file_name)

    # Überprüfen, ob die Datei im Quellordner existiert
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"Datei nicht gefunden: {source_file}")

print("Das Kopieren der Akt-Bilder ist abgeschlossen.")

# KOPIEREN DER GENRE-BILDER PORTRAIT
df_portrait = df[df['genre'].str.contains('portrait', case=False, na=False)]
df_portrait = df_portrait[df_portrait['genre'].str.contains('nude painting') == False]
df_portrait = df_portrait.sample(n=4191)

# Erstellen einer neuen CSV-Datei mit den gefilterten Daten
df_portrait.to_csv('../data/filtered_genres_portrait.csv', index=False)

# Pfad zum Zielordner, in den die gefilterten Bilder kopiert werden sollen
destination_folder_portrait = '../data/zielordner_portrait'

# Kopieren der Bilder Portrait
for file_name in df_portrait['file_name']:
    source_file = os.path.join(source_folder, file_name)
    destination_file = os.path.join(destination_folder_portrait, file_name)

    # Überprüfen, ob die Datei im Quellordner existiert
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"Datei nicht gefunden: {source_file}")

print("Das Kopieren der Portrait-Bilder ist abgeschlossen.")
