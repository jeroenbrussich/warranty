# ./ui_layer/main_menu.py

import ui_layer.helper_functions as helper
from ui_layer.items_menu import display_items_menu


def display_main_menu(db):
    choices = {
        "1": "items beheren",
        # "2": "verkopers beheren",
        # "3" : "lijsten exporteren",
        "q": "de app sluiten",
    }

    while True:
        print("==== HOOFDMENU ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "1":
            display_items_menu(db)

        elif choice == "q" and helper.bevestig(
            "Ben je zeker dat je de app wil sluiten?"
        ):
            return
