import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialisiere die Kaggle API
api = KaggleApi()
api.authenticate()

# Lade den Datensatz herunter
api.dataset_download_files('simolopes/wikiart-all-artpieces', path='kaggle_data', unzip=True)

print("Download abgeschlossen.")
