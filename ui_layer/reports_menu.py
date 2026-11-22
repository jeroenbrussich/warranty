# ./ui_layer/reports_menu.py

import ui_layer.helper_functions as helper
from service_layer.errors import ExportError, NoDataToExportError, StorageError


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
            export_report(report_service.export_items_with_vendors)
        elif choice == "2":
            export_report(report_service.export_items_under_warranty)
        elif choice == "3":
            export_report(report_service.export_items_out_of_warranty)
        elif choice == "q":
            return


def export_report(export):
    try:
        path = export()
    except NoDataToExportError:
        print("Er is geen data om te exporteren.")
    except (ExportError, StorageError) as err:
        print(f"Het rapport werd niet aangemaakt: {err}")
    else:
        print(f"Het rapport werd weggeschreven naar {path}")
