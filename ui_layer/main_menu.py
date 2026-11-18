# ./ui_layer/main_menu.py

import ui_layer.helper_functions as helper


def display_main_menu():
    choices = {
        # "1": "een item toevoegen",
        # "2": "een item wijzigen",
        # "3" : "een lijst met items exporteren",
        # "4": "een verkoper toevoegen",
        # "5": "een verkoper wijzigen",
        # "6" : "een lijst met verkopers exporteren",
        # "7" : "de volledige lijst met items & verkopers exporteren",
        "7": "de app sluiten",
    }

    while True:
        print("==== HOOFDMENU ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "7" and helper.bevestig("Ben je zeker dat je de app wil sluiten?"):
            return
