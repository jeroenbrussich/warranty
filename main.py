# ./main.py
# import locale
import sys

# locale.setlocale(locale.LC_ALL, "nl_BE.UTF-8")

try:
    from data_layer.database import Database
    from service_layer.database_service import DatabaseService
    from service_layer.item_service import ItemService
    from service_layer.report_service import ReportService
    from service_layer.vendor_service import VendorService
    from ui_layer import init_application, main_menu
except ModuleNotFoundError as err:
    if err.name == "settings":
        print(
            "settings.py ontbreekt. Kopieer settings.example.py naar settings.py (zie README)."
        )
    else:
        print(f"Ik kon niet alle benodigde modules inladen: {err}")
    sys.exit(1)


def main():
    print("Applicatie wordt opgestart.")
    db = Database()
    init_application.choose_database(DatabaseService(db))

    main_menu.display_main_menu(ItemService(db), VendorService(db), ReportService(db))


if __name__ == "__main__":
    main()
