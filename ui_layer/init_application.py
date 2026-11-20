# ./ui_layer/init_application.py

import settings
import ui_layer.helper_functions as helper


def choose_database(database_service):
    exists = database_service.exists()
    if exists:
        print(f"- [V] Database {settings.DATABASE_NAME} aanwezig.")
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

    # 1 = nieuwe lege database
    if choice == "1":
        replaced = database_service.create_empty(overwrite=True)
        print(
            "Database vervangen door een leeg exemplaar."
            if replaced
            else "Lege database aangemaakt."
        )

    # 2 = nieuwe database, opgevuld met demodata
    if choice == "2":
        replaced = database_service.create_demo(overwrite=True)
        print(
            "Database vervangen door de demo database."
            if replaced
            else "Demo database aangemaakt."
        )
