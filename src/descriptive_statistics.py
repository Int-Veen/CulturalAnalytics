import pandas as pd
import shutil
import os
import seaborn as sns
import matplotlib.pyplot as plt

#Pfad zur CSV Datei
file_path = '../data/wikiart_art_pieces.csv'
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


#DESCRIPTIVE STATISTICS - DIAGRAMM MIT DER VERTEILUNG DER UNTERSCHIEDLICHEN EPOCHEN FÜR AKTBILDER

# Filtern der Daten, um nur die Zeilen mit "nude painting (nu)" im "genre" zu behalten
nudes_df = pd.read_csv('../data/filtered_genres_nude_painting.csv')

# Zählen der verschiedenen Epochen/Stile
style_counts = nudes_df['style'].value_counts().nlargest(25).reset_index()
style_counts.columns = ['style', 'count']
#s = style_counts[style_counts["count"] > 24]

#Schriftgröße
sns.set(font_scale=1.5)

#Seaborn-Barplots
plt.figure(figsize=(10, 15))
sns.barplot(x='count', y='style', data = style_counts, color="skyblue", linewidth=0.2)

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

plt.savefig("../out/styleplot_pitch.png")

plt.show()
############


