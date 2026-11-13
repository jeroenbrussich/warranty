# ./ui_layer/helper_functions.py


def bevestig(vraag):
    return input(f"{vraag} (j/n): ").strip().lower() == "j"


def vraag_keuze(opties):
    for nummer, omschrijving in opties.items():
        print(f"{nummer}. {omschrijving}")
    keuze = input("Keuze: ").strip()
    while keuze not in opties:
        keuze = input(f"Ongeldige keuze, kies {'/'.join(opties)}: ").strip()
    return keuze
