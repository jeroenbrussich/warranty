# ./settings.py
# Kopieer dit bestand naar settings.py en pas de waarden aan indien nodig.
import os

# ============== DIT MAG JE AANPASSEN
DATA_DIR_NAME = "data"
DATABASE_NAME = "warranty.db"
SEED_FILE_NAME = "demoData.txt"

# ============== HIERONDER NIETS WIJZIGEN
BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(BASE_DIR, DATA_DIR_NAME)
DATABASE_PATH = os.path.join(DATA_DIR, DATABASE_NAME)
SEED_FILE_PATH = os.path.join(DATA_DIR, SEED_FILE_NAME)
