
from datasets import load_dataset
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image
##### ALTER DATENSATZ - ANDERE DATEI NUTZEN -- load kaggle data
sns.set_theme(style="whitegrid")

dataset = load_dataset("huggan/wikiart")
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

print(dataset)
print(dataset["train"].features)
print(dataset["train"].features["genre"])

nude_category = dataset["train"].features['genre'].str2int("nude_painting")
nudes = dataset["train"].filter(lambda x: x["genre"] == nude_category)
nudes_count_styles = {key: 0 for key in dataset["train"].features["style"].names}
count_styles = {key: 0 for key in dataset["train"].features["style"].names}

cwd = os.getcwd()
directory = "../genre_aktbilder"
for i, image in enumerate(nudes):
    print(image)
    path = os.path.join(directory, f"{str(i)}.jpg")
    image["image"].save(path)
    nudes_count_styles[dataset["train"].features['style'].int2str(image["style"])] += 1


# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(10, 15))

# Plot the total styles
sns.set_color_codes("pastel")
sns.barplot(x=list(nudes_count_styles.values()), y=list(nudes_count_styles.keys()), data=nudes_count_styles,
            label="Total", color="b")


# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 600), ylabel="",
       xlabel="Style distribution on nude images")
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.savefig("plot.png")

plt.show()
print(f"Es gibt insgesamt {len(nudes)} Aktbilder.")
print(f"Verteilung der Epochen auf Aktbilder: {nudes_count_styles}")

