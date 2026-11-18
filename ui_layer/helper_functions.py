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


def vraag_tekst(vraag, allow_empty=False):
    while True:
        antwoord = input(vraag).strip()
        if antwoord:
            return antwoord
        if allow_empty:
            return None


def vraag_datum(vraag):
    while True:
        datum_text = input(vraag).strip()
        try:
            datum = datetime.strptime(datum_text, "%d-%m-%Y").date()
        except ValueError:
            print("Geef een geldige datum in.")
            continue
        if datum <= date.today():
            return datum.isoformat()
        print("De datum mag niet in de toekomst liggen.")


def vraag_garantie(vraag):
    while True:
        try:
            garantie = int(input(vraag))
        except ValueError:
            print("Gelieve een geheel getal in te geven.")
            continue
        if garantie >= 0:
            return garantie
        print("Gelieve een geheel getal in te geven.")


def vraag_vendor(vendors, vraag):
    choices = {str(vendor.vendor_id): vendor.vendor_name for vendor in vendors}
    choices["0"] = "annuleren"
    print(vraag)
    choice = vraag_keuze(choices)
    if choice == "0":
        return None
    return int(choice)
