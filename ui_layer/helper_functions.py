# ./ui_layer/helper_functions.py

from datetime import date, datetime


def bevestig(vraag):
    return input(f"{vraag} (j/n): ").strip().lower() == "j"


def vraag_keuze(opties):
    for nummer, omschrijving in opties.items():
        print(f"{nummer}. {omschrijving}")
    keuze = input("Keuze: ").strip()
    while keuze not in opties:
        keuze = input(f"Ongeldige keuze, kies {'/'.join(opties)}: ").strip()
    return keuze


def vraag_tekst(vraag, allow_empty=False, default=None):
    if default is not None:
        wissen = ", - = wissen" if allow_empty else ""
        vraag += f"[enter = {default}{wissen}] "
    elif allow_empty:
        vraag += "[enter om over te slaan] "

    while True:
        antwoord = input(vraag).strip()
        if antwoord == "-" and allow_empty and default is not None:
            return None
        if antwoord:
            return antwoord
        if default is not None:
            return default
        if allow_empty:
            return None


def vraag_datum(vraag, default=None):
    if default is not None:
        vraag += f"[enter = {date.fromisoformat(default).strftime('%d-%m-%Y')}] "

    while True:
        datum_text = input(vraag).strip()
        if not datum_text and default is not None:
            return default
        try:
            datum = datetime.strptime(datum_text, "%d-%m-%Y").date()
        except ValueError:
            print("Geef een geldige datum in.")
            continue
        if datum <= date.today():
            return datum.isoformat()
        print("De datum mag niet in de toekomst liggen.")


def vraag_garantie(vraag, default=None):
    if default is not None:
        vraag += f"[enter = {default}] "

    while True:
        antwoord = input(vraag).strip()
        if not antwoord and default is not None:
            return default
        try:
            garantie = int(antwoord)
        except ValueError:
            print("Gelieve een geheel getal in te geven.")
            continue
        if garantie >= 0:
            return garantie
        print("De garantie kan niet negatief zijn.")


def vraag_vendor(vendors, vraag):
    choices = {str(vendor.vendor_id): vendor.vendor_name for vendor in vendors}
    choices["0"] = "annuleren"
    print(vraag)
    choice = vraag_keuze(choices)
    if choice == "0":
        return None
    return int(choice)


def vraag_item(items, vraag):
    choices = {
        str(item.item_id): f"{item.item_name} ({item.item_make} {item.item_model})"
        for item in items
    }
    choices["0"] = "annuleren"
    print(vraag)
    choice = vraag_keuze(choices)
    if choice == "0":
        return None
    for item in items:
        if str(item.item_id) == choice:
            return item
