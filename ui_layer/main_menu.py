# ./ui_layer/main_menu.py

import ui_layer.helper_functions as helper


def display_main_menu():
    choices = {
        # "1": "een item toevoegen",
        # "2": "een item wijzigen",
        # "3" : "items exporteren",
        "4": "de app sluiten",
    }

    while True:
        print("==== HOOFDMENU ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "4" and helper.bevestig("Ben je zeker dat je de app wil sluiten?"):
            return
