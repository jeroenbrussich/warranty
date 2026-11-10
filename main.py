# ./main.py
import sys

try:
    import settings
    from data_layer.database import Database
    from data_layer.seed import Seed
except ModuleNotFoundError as err:
    if err.name == "settings":
        print(
            "settings.py ontbreekt. Kopieer settings.example.py naar settings.py (zie README)."
        )
    else:
        print(f"Ik kon niet alle benodigde modules inladen: {err}")
    sys.exit(1)


def vraag_keuze(opties):
    for nummer, omschrijving in opties.items():
        print(f"{nummer}. {omschrijving}")
    keuze = input("Keuze: ").strip()
    while keuze not in opties:
        keuze = input(f"Ongeldige keuze, kies {'/'.join(opties)}: ").strip()
    return keuze


def bevestig(vraag):
    return input(f"{vraag} (j/n): ").strip().lower() == "j"


def database_menu(db):
    bestaat = db.exists()
    if bestaat:
        print(f"- [x] Database {settings.DATABASE_NAME} aanwezig.")
        opties = {
            "1": "vervangen door een lege database",
            "2": "vervangen door de demo database",
            "3": "behouden",
        }
    else:
        print(f"- [-] Database {settings.DATABASE_NAME} ontbreekt.")
        opties = {
            "1": "een lege database aanmaken",
            "2": "de demo database aanmaken",
        }

    print("Wat wens je te doen?")
    keuze = vraag_keuze(opties)

    # 3 = doorgaan
    if keuze == "3":
        return

    # niet 3 + bestaat = destructieve actie
    if bestaat and not bevestig("De bestaande database gaat verloren. Doorgaan?"):
        print("Niets gewijzigd.")
        return

    # 1/2 = nieuwe lege database
    if keuze in ("1", "2"):
        vervangen = db.create(overwrite=True)
        print(
            "Database vervangen door een leeg exemplaar."
            if vervangen
            else "Lege database aangemaakt."
        )

    # 2 = lege database opvullen
    if keuze == "2":
        seed = Seed(db)
        seed.import_seed_file()


def main():
    print("Applicatie wordt opgestart.")
    database_menu(Database())


if __name__ == "__main__":
    main()
