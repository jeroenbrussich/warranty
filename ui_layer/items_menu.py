# ./ui_layer/items_menu.py

import ui_layer.helper_functions as helper
from domain_layer.item import Item
from service_layer.errors import StorageError
from service_layer.item_service import DuplicateSerialError


def display_items_menu(item_service, vendor_service, report_service):
    choices = {
        "0": "een overzicht opvragen",
        "1": "een item toevoegen",
        "2": "een item wijzigen",
        # "3" : "een item verwijderen",
        "q": "terugkeren naar het hoofdmenu",
    }

    while True:
        print("==== MENU: ITEMS ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "0":
            show_items(report_service)
        elif choice == "1":
            create_item(item_service, vendor_service)
        elif choice == "2":
            edit_item(item_service, vendor_service)
        elif choice == "q":
            return


def show_items(report_service):
    items = report_service.get_items_with_vendor_and_warranty_end_date()
    if not len(items):
        print("De database bevat nog geen gegevens.")
        return

    print()
    print(f"| {'—' * 15} | {'—' * 15} | {'—' * 15} | {'—' * 15} | {'—' * 15} |")
    print(
        f"| {'naam':^15} | {'fabrikant':^15} | {'type':^15} | {'aangekocht':^15} | {'einde garantie':^15} |"
    )
    print(f"| {'_' * 15} | {'_' * 15} | {'_' * 15} | {'_' * 15} | {'_' * 15} |")
    for item in items:
        print(
            f"| {item['item_name']:<15} | {item['item_make']:<15} | {item['item_model']:<15} | {item['item_date_bought']:<15} | {item['item_warranty_end']:<15} |"
        )
    print(f"| {'_' * 15} | {'_' * 15} | {'_' * 15} | {'_' * 15} | {'_' * 15} | ")
    print()


def create_item(item_service, vendor_service):
    item = collect_item_fields(vendor_service)
    if item is None:
        return

    try:
        item_service.add_item(item)
    except DuplicateSerialError:
        print("Er bestaat al een item met dit serienummer.")
    except StorageError as err:
        print(f"Het item werd niet toegevoegd: {err}")
    else:
        print("Item toegevoegd.")


def edit_item(item_service, vendor_service):
    items = item_service.get_all_items()
    if not items:
        print("Er zijn nog geen items.")
        return

    current = helper.vraag_item(items, "Welk item wil je wijzigen?")
    if current is None:
        print("Wijzigen geannuleerd.")
        return

    updated = collect_item_fields(vendor_service, current)
    if updated is None:
        return

    try:
        item_service.update_item(updated)
    except DuplicateSerialError:
        print("Er bestaat al een item met dit serienummer.")
    except StorageError as err:
        print(f"Het item werd niet gewijzigd: {err}")
    else:
        print("Item gewijzigd.")


def collect_item_fields(vendor_service, current=None):
    vendors = vendor_service.get_all_vendors()
    if not vendors:
        print("Er zijn nog geen verkopers. Voeg eerst een verkoper toe.")
        return None

    if current is None:
        vendor_id = helper.vraag_vendor(
            vendors, "Bij welke verkoper heb je dit item gekocht?"
        )
        if vendor_id is None:
            print("Toevoegen geannuleerd.")
            return None
        defaults = Item(
            item_name=None,
            item_make=None,
            item_model=None,
            item_date_bought=None,
            item_warranty=None,
            vendor_id=None,
        )
    else:
        defaults = current
        vendor_id = current.vendor_id
        vendor_names = {vendor.vendor_id: vendor.vendor_name for vendor in vendors}
        if helper.bevestig(f"De verkoper is nu {vendor_names[vendor_id]}. Wijzigen?"):
            chosen = helper.vraag_vendor(vendors, "Welke verkoper moet het worden?")
            if chosen is not None:
                vendor_id = chosen

    name = helper.vraag_tekst(
        "Welke naam wil je aan dit item geven? ", default=defaults.item_name
    )

    serial = helper.vraag_tekst(
        "Wat is het serienummer van dit item? ",
        allow_empty=True,
        default=defaults.item_serial,
    )

    make = helper.vraag_tekst(
        "Wie is de fabrikant van dit item? ", default=defaults.item_make
    )

    model = helper.vraag_tekst(
        "Wat is het type van dit item? ", default=defaults.item_model
    )

    date_bought = helper.vraag_datum(
        "Wanneer heb je dit item aangekocht? Geef de datum in volgens het formaat dd-mm-jjjj ",
        default=defaults.item_date_bought,
    )

    warranty = helper.vraag_garantie(
        "Hoeveel maanden garantie heb je op dit item? ",
        default=defaults.item_warranty,
    )

    return Item(
        item_id=defaults.item_id,
        item_name=name,
        item_serial=serial,
        item_make=make,
        item_model=model,
        item_date_bought=date_bought,
        item_warranty=warranty,
        vendor_id=vendor_id,
    )
