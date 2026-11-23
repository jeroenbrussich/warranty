# ./ui_layer/main_menu.py

import ui_layer.helper_functions as helper
from ui_layer.items_menu import display_items_menu
from ui_layer.reports_menu import display_reports_menu
from ui_layer.vendors_menu import display_vendors_menu


def display_main_menu(item_service, vendor_service, report_service):
    choices = {
        "1": "items beheren",
        "2": "verkopers beheren",
        "3": "lijsten exporteren",
        "q": "de app sluiten",
    }

    while True:
        print("==== HOOFDMENU ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "1":
            display_items_menu(item_service, vendor_service, report_service)
        elif choice == "2":
            display_vendors_menu(vendor_service, report_service)
        elif choice == "3":
            display_reports_menu(report_service)
        elif choice == "q" and helper.bevestig(
            "Ben je zeker dat je de app wil sluiten?"
        ):
            return
