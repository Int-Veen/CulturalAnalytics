import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.set_option('display.max_columns', None)

df = pd.read_csv("prompt_result_with_gender_df.csv")

passive_verbs = ['lying', 'resting', 'laying', 'reclining', 'relaxing', 'sleeping']
active_verbs = ['standing', 'leaning', 'walking', 'preparing', 'playing', 'reaching', 'flying', 'running', 'fishing',
                'carrying', 'dining', 'combing', 'drinking', 'participating', 'sharing', 'riding', 'building']
neutral_verbs = ['sitting', 'wearing', 'holding', 'looking', 'enjoying', 'looking', 'setting', 'drawing', 'facing',
                 'including', 'clothing', 'something', 'observing', 'indicating', 'engaging', 'creating', 'reading',
                 'taking', 'adding', 'waiting', 'being', 'admiring', 'studying', 'socializing', 'watching', 'living',
                 'appealing', 'contemplating', 'gathering', 'discussing', 'surrounding', 'sharing', 'suggesting',
                 'flowing', 'smiling', 'interacting', 'containing', 'using', 'smoking']
sexual_verbs = ['kneeling', 'bending', 'posing', 'swimming', 'bathing', 'covering', 'drying', 'dancing', 'washing',
                'embracing', 'floating', 'stretching', 'hugging', 'loving']

df['active_verb'] = False
df['passive_verb'] = False
df['neutral_verb'] = False
df['sexual_verb'] = False

# Durch jede Zeile in der Spalte 'answer' iterieren
for index, row in df.iterrows():
    active_flag, passive_flag, sexual_flag, neutral_flag = False, False, False, False
    char_remove = [".", ","]
    for char in char_remove:
        myanswer = row['answer'].lower().replace(char, "").split(" ")
    for word in myanswer:
        for keyword in active_verbs:
            if keyword == word:
                active_flag = True

        for keyword in passive_verbs:
            if keyword == word:
                passive_flag = True

        for keyword in neutral_verbs:
            if keyword == word:
                neutral_flag = True

        for keyword in sexual_verbs:
            if keyword == word:
                sexual_flag = True

    df.at[index, 'active_verb'] = active_flag
    df.at[index, 'passive_verb'] = passive_flag
    df.at[index, 'neutral_verb'] = neutral_flag
    df.at[index, 'sexual_verb'] = sexual_flag

print(df['active_verb'].value_counts())
print(df['passive_verb'].value_counts())
print(df['neutral_verb'].value_counts())
print(df['sexual_verb'].value_counts())

# df.to_csv('./prompt_result_with_gender_BP_df.csv', index=False)

####################################################################
###                   DATAFRAME SEXUAL                           ###
####################################################################

unknown_sexual = (df['kosmos_gender'] == 'unknown') & (df['sexual_verb'] == True)
female_sexual = (df['kosmos_gender'] == 'female') & (df['sexual_verb'] == True)
male_sexual = (df['kosmos_gender'] == 'male') & (df['sexual_verb'] == True)
female_and_male_sexual = (df['kosmos_gender'] == 'female-and-male') & (df['sexual_verb'] == True)

print(len(df.loc[unknown_sexual, 'sexual_verb']))
print(len(df.loc[female_sexual, 'sexual_verb']))
print(len(df.loc[male_sexual, 'sexual_verb']))
print(len(df.loc[female_and_male_sexual, 'sexual_verb']))

unknown_sexual = (df['kosmos_gender'] == 'unknown') & (df['sexual_verb'] == False)
female_sexual = (df['kosmos_gender'] == 'female') & (df['sexual_verb'] == False)
male_sexual = (df['kosmos_gender'] == 'male') & (df['sexual_verb'] == False)
female_and_male_sexual = (df['kosmos_gender'] == 'female-and-male') & (df['sexual_verb'] == False)

print(len(df.loc[unknown_sexual, 'sexual_verb']))
print(len(df.loc[female_sexual, 'sexual_verb']))
print(len(df.loc[male_sexual, 'sexual_verb']))
print(len(df.loc[female_and_male_sexual, 'sexual_verb']))


####################################################################
###                        SEXUAL PLOT                           ###
####################################################################
print(type(df[df['sexual_verb'] == True]['kosmos_gender']))
df[df['sexual_verb'] == True]['kosmos_gender'].value_counts()
#d f[df['sexual_verb'] == True]['kosmos_gender'].value_counts().plot(kind = 'bar', title = 'Verteilung der sexualisierten Verben nach Geschlecht')

# DIAGRAMM
gender_category = ['unknown', 'female', 'male', 'female-and-male']
gender_category_counts = [213, 114, 15, 62] # True: [213, 114, 15, 62]  False: [1985, 825, 151, 826]
color_balken = '#4169e1',
fig, ax = plt.subplots()
bar_container = ax.bar(gender_category, gender_category_counts, color= color_balken)
ax.set(ylabel='Anzahl Aktbilder mit sexualisierter Pose', title='Genderunterschiede in sexualisierten Posen', ylim=(0,250))
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.show()

#print("Hier beginnt: Sexual")
#print(df[df['sexual_verb'] == False]['kosmos_gender'].value_counts())
#print(df[df['sexual_verb'] == True]['kosmos_gender'].value_counts())

####################################################################
###                 DATAFRAME PASSIV, ACTIVE, NORMAL             ###
####################################################################
print("Hier beginnt: Passiv - False ")
print(df[df['passive_verb'] == False]['kosmos_gender'].value_counts())
print("Hier beginnt: Passiv - True ")
print(df[df['passive_verb'] == True]['kosmos_gender'].value_counts())

print("Hier beginnt: Aktiv - False ")
print(df[df['active_verb'] == False]['kosmos_gender'].value_counts())
print("Hier beginnt: Aktiv - True ")
print(df[df['active_verb'] == True]['kosmos_gender'].value_counts())

print("Hier beginnt: Neutral - False ")
print(df[df['neutral_verb'] == False]['kosmos_gender'].value_counts())
print("Hier beginnt: Neutral - True ")
print(df[df['neutral_verb'] == True]['kosmos_gender'].value_counts())

# DIAGRAMM PASSIV
gender_category = ['unknown','female-and-male', 'female', 'male',]
gender_category_counts = [603, 307, 296, 33]
color_balken = '#4169e1',
fig, ax = plt.subplots()
bar_container = ax.bar(gender_category, gender_category_counts, color= color_balken)
ax.set(ylabel='Anzahl Aktbilder mit passiver Pose', title='Genderunterschiede in passiven Posen', ylim=(0, 650))
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.show()

# DIAGRAMM AKTIV
gender_category = ['unknown','female-and-male', 'female', 'male',]
gender_category_counts = [1848, 651, 746, 134]
color_balken = '#4169e1',
fig, ax = plt.subplots()
bar_container = ax.bar(gender_category, gender_category_counts, color= color_balken)
ax.set(ylabel='Anzahl Aktbilder mit aktiver Pose', title='Genderunterschiede in aktiven Posen', ylim=(0, 2000))
ax.bar_label(bar_container, fmt='{:,.0f}')
plt.show()


