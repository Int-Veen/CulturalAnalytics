import pandas as pd
import re
from collections import Counter

df = pd.read_csv("prompt_result_final.csv")

found_words = []

for answer in df['answer']:
    words = re.findall(r'\b\w+ing\b', answer)
    found_words.extend(words)

word_counts = Counter(found_words)
most_common_30 = word_counts.most_common(30)

#Ergebnis
for word, count in most_common_30:
    print(f"{word}' : {count}")