import pandas as pd
import shutil
import os
import seaborn as sns
import matplotlib.pyplot as plt

#Pfad zur CSV Datei
file_path = '/Users/int-veen/Documents/CulturalAnalytics/Kaggle_archive2/wikiart_art_pieces.csv'
d = {}

#CSV-Datei einlesen
df = pd.read_csv(file_path)
# Zählen, wie oft "nude painting (nu)" in der Spalte "genre" vorkommt
for g in df["genre"]:
    for x in g.split(","):
        d[x] = True

print(len(d))
nude_painting_count = df[df['genre'] == 'nude painting (nu)'].shape[0]

print(f"Anzahl der Bilder vom Genre 'nude painting (nu)': {nude_painting_count}")

# Zählen, wie oft der String "nude painting (nu)" in der Spalte "genre" vorkommt
nude_painting_count = df['genre'].str.contains('nude painting \(nu\)', case=False, na=False).sum()
print(f"Anzahl der Bilder vom Genre 'nude painting (nu)', einschließlich Kombinationen: {nude_painting_count}")

# Zählen, wie oft der String "portrait" in der Spalte "genre" vorkommt
portrait_count = df['genre'].str.contains('portrait', case=False, na=False).sum()
print(f"Anzahl der Bilder vom Genre 'portrait', einschließlich Kombinationen: {portrait_count}")


# Filtern der Daten, um nur die Zeilen mit "nude painting (nu)" und "portrait" im "genre" zu behalten
filtered_df = df[df['genre'].str.contains('nude painting \(nu\)|portrait', case=False, na=False)]

# Erstellen einer neuen CSV-Datei mit den gefilterten Daten
filtered_df.to_csv('filtered_genres_with_all_columns.csv', index=False)

print("Die gefilterte Datei wurde erstellt und als 'filtered_genres_with_all_columns.csv' gespeichert.")

## KOPIEREN DER BILDER VON NUDE PAINTING UND PORTRAIT

# Pfad zur gefilterten CSV-Datei
csv_file_path = '/Users/int-veen/Documents/CulturalAnalytics/datensatz/filtered_genres_with_all_columns.csv'

# Pfad zum Quellordner, wo sich alle Bilder befinden
source_folder = '/Users/int-veen/Documents/CulturalAnalytics/Kaggle_archive2/wikiart/wikiart'

# Pfad zum Zielordner, in den die gefilterten Bilder kopiert werden sollen
destination_folder = '/Users/int-veen/Documents/CulturalAnalytics/Zielordner_Kaggle_archive2'

# CSV-Datei einlesen
df = pd.read_csv(csv_file_path)

# Kopieren der Bilder
for file_name in df['file_name']:
    source_file = os.path.join(source_folder, file_name)
    destination_file = os.path.join(destination_folder, file_name)

    # Überprüfen, ob die Datei im Quellordner existiert
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"Datei nicht gefunden: {source_file}")

print("Das Kopieren der Bilder ist abgeschlossen.")


#DESCRIPTIVE STATISTICS - DIAGRAMM MIT DER VERTEILUNG DER UNTERSCHIEDLICHEN EPOCHEN FÜR AKTBILDER

# Pfad zur hochgeladenen CSV-Datei
c_file_path = '/Users/int-veen/Documents/CulturalAnalytics/datensatz/filtered_genres_with_all_columns.csv'

# CSV einlesen
df = pd.read_csv(c_file_path)

# Filtern der Daten, um nur die Zeilen mit "nude painting (nu)" im "genre" zu behalten
nudes_df = df[df['genre'].str.contains('nude painting \(nu\)', case=False, na=False)]

# Zählen der verschiedenen Epochen/Stile
style_counts = nudes_df['style'].value_counts().reset_index()
style_counts.columns = ['style', 'count']
s = style_counts[style_counts["count"] > 40]

#Schriftgröße
sns.set(font_scale=1.5)

#Seaborn-Barplots
plt.figure(figsize=(10, 15))
sns.barplot(x='count', y='style', data=s, color="skyblue", linewidth=0.2)

# Titel und Achsenbeschriftungen
plt.title('Verteilung der Epochen auf Aktbilder', fontsize=20)
plt.xlabel('Anzahl der Bilder')
plt.ylabel('Epoche/Stil', fontsize= 16)

#plt.xticks(fontsize=20, weight='bold')
#plt.yticks(fontsize=20,weight='bold') #Y Achse

# Entfernen der Achsenränder
sns.despine(left=True, bottom=True)
sns.set(font_scale=2.5)
plt.tight_layout()

plt.savefig("styleplot_pitch.png")

plt.show()


