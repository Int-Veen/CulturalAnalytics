import pandas as pd

df = pd.read_csv("prompt_result_final.csv")
df_nudenet = pd.read_csv("../nudenet/nude_paintings_detections.csv")

# Umbenennen der Spalte 'file_name' in 'filename' um Konsistenz zu schaffen
df_nudenet.rename(columns={'file_name': 'filename'}, inplace=True)

# Benenne die Spalte 'gender' in 'nudenet_gender' um
df_nudenet = df_nudenet.rename(columns={'gender': 'nudenet_gender'})

# Verknüpfe die DataFrames auf Basis der 'filename' Spalte
prompt_result_with_gender_df = pd.merge(df, df_nudenet[['filename', 'nudenet_gender']], on='filename', how='left')

MALES = ["male", "boy", "men", "man", "males", "boys", "he", "him", "his", "he's"]
FEMALES = ["female", "girl", "women", "woman", "females", "girls", "she", "her", "hers", "she's"]

# Durch jede Zeile in der Spalte 'answer' iterieren
for index, row in prompt_result_with_gender_df.iterrows():
    male_flag, female_flag = False, False
    char_remove = [".", ","]
    for char in char_remove:
        myanswer = row['answer'].lower().replace(char, "").split(" ")
    for word in myanswer:
        for male_keyword in MALES:
            if male_keyword == word:
                male_flag = True

        for female_keyword in FEMALES:
            if female_keyword == word:
                female_flag = True

    if male_flag and female_flag:
        prompt_result_with_gender_df.at[index, 'kosmos_gender'] = 'female-and-male'
    elif male_flag and not female_flag:
        prompt_result_with_gender_df.at[index, 'kosmos_gender'] = 'male'
    elif not male_flag and female_flag:
        prompt_result_with_gender_df.at[index, 'kosmos_gender'] = 'female'
    else:
        prompt_result_with_gender_df.at[index, 'kosmos_gender'] = 'unknown'

print(prompt_result_with_gender_df['kosmos_gender'].value_counts())

prompt_result_with_gender_df.to_csv('./prompt_result_with_gender_df.csv', index=False)
