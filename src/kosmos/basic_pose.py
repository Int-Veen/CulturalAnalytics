import pandas as pd
df = pd.read_csv("prompt_result_final.csv")

basic_pose = ['standing', 'sleeping', 'lying', 'sitting']

# Initialisierung neuer Spalten für das Geschlecht
df['female'] = 0
df['male'] = 0
df['women'] = 0
df['men'] = 0
df['girl'] = 0
df['boy'] = 0

# Durch jede Zeile in der Spalte 'answer' iterieren
for index, row in df.iterrows():
    df.at[index, 'female'] = row['answer'].lower().count('female')
    df.at[index, 'male'] = row['answer'].lower().count('male')
    df.at[index, 'women'] = row['answer'].lower().count('women')
    df.at[index, 'men'] = row['answer'].lower().count('men')
    df.at[index, 'girl'] = row['answer'].lower().count('girl')
    df.at[index, 'boy'] = row['answer'].lower().count('boy')

results_list = []

# Durchlaufen jeder Zeile, um die Grundpose und Geschlechterhäufigkeit zu sammeln
for index, row in df.iterrows():
    for word in basic_pose:
        if word in row['answer']:
            count = row['answer'].count(word)
            #Änderung: Geschlechterhäufigkeiten hinzufügen
            results_list.append({
                'filename': row['filename'],
                'word': word,
                'occurrences': count,
                'female': row['female'],
                'male': row['male'],
                'women': row['women'],
                'men': row['men'],
                'girl': row['girl'],
                'boy': row['boy'],
                # Bestimmung des Geschlechts basierend auf den Zählungen
                'prompt_Gender': 'female' if row['female'] > 0 or row['women'] > 0 or row['girl'] > 0 else
                                ('male' if row['male'] > 0 or row['men'] > 0 or row['boy'] > 0 else 'unknown')
            })

results_df=pd.DataFrame(results_list, columns=['filename', 'word', 'occurrences', 'female', 'male','women','men',
                                               'girl', 'boy', 'prompt_Gender'])
results_df.to_csv('/Users/int-veen/Documents/CulturalAnalytics/src/kosmos/basicpose.csv', index=False)

print(results_df)

# Zähle wie oft jeder Wert in der Spalte 'prompt_Gender' vorkommt
df = pd.read_csv('basicpose.csv')
gender_counts = df['prompt_Gender'].value_counts()
print(gender_counts)

####################################################################

basicpose_df = pd.read_csv('basicpose.csv')
nude_paintings_df = pd.read_csv('/Users/int-veen/Documents/CulturalAnalytics/src/nudenet/nude_paintings_detections.csv')

# Umbenennen der Spalte 'file_name' in 'filename' um Konsistenz zu schaffen
nude_paintings_df.rename(columns={'file_name': 'filename'}, inplace=True)

# Benenne die Spalte 'gender' in 'nudenet_gender' um
nude_paintings_df = nude_paintings_df.rename(columns={'gender': 'nudenet_gender'})

# Verknüpfe die DataFrames auf Basis der 'filename' Spalte
combined_df = pd.merge(basicpose_df, nude_paintings_df[['filename', 'nudenet_gender']], on='filename', how='left')
combined_df.to_csv('/Users/int-veen/Documents/CulturalAnalytics/src/kosmos/updated_basicpose.csv', index=False)

####################################################################
###                DESCRIPTIVE STATISTICS                        ###
####################################################################

result_gender_difference = []
# Für jedes Wort in basic_pose die Verteilung von nudenet_gender zählen
for word in basic_pose:
    filtered_df = combined_df[combined_df['word'] == word]
# Gruppierung nach nudenet_gender und das Vorkommen zählen
    # gender_counts = filtered_df.groupby('nudenet_gender').size()
    gender_counts = filtered_df['nudenet_gender'].value_counts().reset_index()
    gender_counts.columns = ['nudenet_gender', 'count']

    gender_counts['word'] = word
    result_gender_difference.append(gender_counts)

result_gender_df = pd.concat(result_gender_difference, ignore_index=True)
result_gender_df.to_csv("/Users/int-veen/Documents/CulturalAnalytics/src/kosmos/gender_difference.csv", index=False)



