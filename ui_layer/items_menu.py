# ./ui_layer/items_menu.py

import ui_layer.helper_functions as helper
from domain_layer.item import Item
from service_layer.item_service import DuplicateSerialError, ItemService
from service_layer.vendor_service import VendorService


def display_items_menu(db):

    choices = {
        "1": "een item toevoegen",
        # "2": "een item wijzigen",
        # "3" : "een item verwijderen",
        "4": "terugkeren naar het hoofdmenu",
    }
    item_service = ItemService(db)

    while True:
        print("==== MENU: ITEMS ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "1":
            item = collect_item_fields(db)
            if item is not None:
                try:
                    item_service.add_item(item)
                except DuplicateSerialError:
                    print("Er bestaat al een item met dit serienummer.")
                else:
                    print("Item toegevoegd.")
        elif choice == "4":
            return


def collect_item_fields(db):

    vendor_service = VendorService(db)

    vendors = vendor_service.get_all_vendors()
    if not vendors:
        print("Er zijn nog geen verkopers. Voeg eerst een verkoper toe.")
        return None

    vendor_id = helper.vraag_vendor(
        vendors, "Bij welke verkoper heb je dit item gekocht?"
    )

    if vendor_id is None:
        print("Toevoegen geannuleerd.")
        return None

    name = helper.vraag_tekst("Welke naam wil je aan dit item geven? ")

    serial = helper.vraag_tekst(
        "Wat is het serienummer van dit item? [enter om over te slaan] ",
        allow_empty=True,
    )

    make = helper.vraag_tekst("Wie is de fabrikant van dit item? ")

    model = helper.vraag_tekst("Wat is het type van dit item? ")

    date_bought = helper.vraag_datum(
        "Wanneer heb je dit item aangekocht? Geef de datum in volgens het formaat dd-mm-jjjj "
    )

    warranty = helper.vraag_garantie("Hoeveel maanden garantie heb je op dit item? ")

    return Item(
        item_name=name,
        item_serial=serial,
        item_make=make,
        item_model=model,
        item_date_bought=date_bought,
        item_warranty=warranty,
        vendor_id=vendor_id,
    )
