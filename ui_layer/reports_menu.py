# ./ui_layer/reports_menu.py

import ui_layer.helper_functions as helper
from service_layer.errors import StorageError


def display_reports_menu(report_service):
    choices = {
        "1": "alle items met hun verkoper exporteren",
        "2": "alle items onder garantie exporteren",
        "3": "alle items buiten garantie exporteren",
        "q": "terugkeren naar het hoofdmenu",
    }

    while True:
        print("==== MENU: RAPPORTEN ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "1":
            export_items_with_vendors(report_service)
        elif choice == "2":
            export_items_under_warranty(report_service)
        elif choice == "3":
            export_items_out_of_warranty(report_service)
        elif choice == "q":
            return


def export_items_with_vendors(report_service):
    try:
        path = report_service.export_items_with_vendors()
    except StorageError as err:
        print(f"Het rapport werd niet aangemaakt: {err}")
    else:
        print(f"Het rapport werd weggeschreven naar {path}")


def export_items_under_warranty(report_service):
    try:
        path = report_service.export_items_under_warranty()
    except StorageError as err:
        print(f"Het rapport werd niet aangemaakt: {err}")
    else:
        print(f"Het rapport werd weggeschreven naar {path}")


def export_items_out_of_warranty(report_service):
    try:
        path = report_service.export_items_out_of_warranty()
    except StorageError as err:
        print(f"Het rapport werd niet aangemaakt: {err}")
    else:
        print(f"Het rapport werd weggeschreven naar {path}")
