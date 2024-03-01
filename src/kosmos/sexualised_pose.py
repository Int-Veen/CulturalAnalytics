import pandas as pd
df = pd.read_csv("prompt_result_final.csv")

sexual_pose = [ 'undress*', 'bathing', 'seductive pose', 'sensual*', 'concealed nud*', 'danc*', 'nude', 'provocative',
                'sexualised', 'sexual', 'kneeling']

results_list = []
# Durch jede Zeile in der Spalte 'answer' iterieren
for index, row in df.iterrows():
    for word in sexual_pose:
        if word in row['answer']:
            count = row['answer'].count(word)
            results_list.append({
                'filename': row['filename'],
                'word': word,
                'occurrences': count
            })

results_df=pd.DataFrame(results_list, columns=['filename', 'word', 'occurrences'])
results_df.to_csv('/Users/int-veen/Documents/CulturalAnalytics/src/kosmos/sexualised_pose.csv')

print(results_df)