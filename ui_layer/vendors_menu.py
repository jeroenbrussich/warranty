# ./ui_layer/vendors_menu.py

import ui_layer.helper_functions as helper
from domain_layer.vendor import Vendor
from service_layer.errors import StorageError
from service_layer.vendor_service import DuplicateVendorNameError


def display_vendors_menu(vendor_service):
    choices = {
        "1": "een verkoper toevoegen",
        "2": "een verkoper wijzigen",
        # "3" : "een verkoper verwijderen",
        "q": "terugkeren naar het hoofdmenu",
    }

    while True:
        print("==== MENU: VERKOPERS ====")
        print("Ik wil")
        choice = helper.vraag_keuze(choices)

        if choice == "1":
            create_vendor(vendor_service)
        elif choice == "2":
            edit_vendor(vendor_service)
        elif choice == "q":
            return


def create_vendor(vendor_service):
    vendor = collect_vendor_fields()

    if vendor is None:
        return

    try:
        vendor_service.add_vendor(vendor)
        print("De verkoper werd toegevoegd.")
    except DuplicateVendorNameError:
        print(f"Er bestaat al een verkoper met de naam '{vendor.vendor_name}'.")
    except StorageError as err:
        print(f"De verkoper werd niet toegevoegd: {err}")


def edit_vendor(vendor_service):
    vendors = vendor_service.get_all_vendors()

    if not vendors:
        print("Er zijn nog geen verkopers. Voeg eerst een verkoper toe.")
        return

    vendor_id = helper.vraag_vendor(vendors, "Welke verkoper wil je wijzigen?")
    if vendor_id is None:
        print("Wijzigen geannuleerd.")
        return

    current = None
    for vendor in vendors:
        if vendor.vendor_id == vendor_id:
            current = vendor
            break
    updated = collect_vendor_fields(current)

    try:
        vendor_service.update_vendor(updated)
        print("De verkoper werd gewijzigd.")
    except DuplicateVendorNameError:
        print(f"Er bestaat al een verkoper met de naam '{updated.vendor_name}'.")
    except StorageError as err:
        print(f"De verkoper werd niet gewijzigd: {err}")


def collect_vendor_fields(current=None):
    name = helper.vraag_tekst(
        "Wat is de naam van de verkoper? ",
        default=current.vendor_name if current else None,
    )
    url = helper.vraag_tekst(
        "Wat is de eventuele website voor deze winkel? ",
        allow_empty=True,
        default=current.vendor_url if current else None,
    )
    is_webshop = helper.bevestig(
        "Deze winkel is een webshop",
        default=current.vendor_is_webshop if current else None,
    )

    return Vendor(
        vendor_id=current.vendor_id if current else None,
        vendor_name=name,
        vendor_url=url,
        vendor_is_webshop=is_webshop,
    )
