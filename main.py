# ./main.py
import sys

try:
    import ui_layer.init_application as init
    from data_layer.database import Database
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
    init.choose_database(Database())


if __name__ == "__main__":
    main()
