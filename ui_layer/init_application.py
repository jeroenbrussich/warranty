# ./ui_layer/init_application.py

import settings
import ui_layer.helper_functions as helper
from service_layer.seed import Seed


def choose_database(db):
    exists = db.exists()
    if exists:
        print(f"- [x] Database {settings.DATABASE_NAME} aanwezig.")
        choices = {
            "1": "vervangen door een lege database",
            "2": "vervangen door de demo database",
            "3": "behouden",
        }
    else:
        print(f"- [-] Database {settings.DATABASE_NAME} ontbreekt.")
        choices = {
            "1": "een lege database aanmaken",
            "2": "de demo database aanmaken",
        }

    print("Wat wens je te doen?")
    choice = helper.vraag_keuze(choices)

    # 3 = doorgaan
    if choice == "3":
        return

    # niet 3 + bestaat = destructieve actie
    if exists and not helper.bevestig("De bestaande database gaat verloren. Doorgaan?"):
        print("Niets gewijzigd.")
        return

    # 1/2 = nieuwe lege database
    if choice in ("1", "2"):
        replaced = db.create(overwrite=True)
        print(
            "Database vervangen door een leeg exemplaar."
            if replaced
            else "Lege database aangemaakt."
        )

    # 2 = lege database opvullen
    if choice == "2":
        seed = Seed(db)
        seed.import_seed_file()
