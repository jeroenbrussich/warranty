# ./main.py
import sys

try:
    from data_layer.database import Database
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
    init_application.choose_database(Database())

    main_menu.display_main_menu()


if __name__ == "__main__":
    main()
