# ./service_layer/database_service.py

from service_layer.seed import Seed


class DatabaseService:
    def __init__(self, database):
        self.__database = database

    def exists(self):
        return self.__database.exists()

    def create_empty(self, overwrite=False):
        """Maak een lege database. Geeft True terug als een bestaande vervangen werd.

        Gooit FileExistsError als de database bestaat en overwrite False is.
        """
        return self.__database.create(overwrite=overwrite)

    def create_demo(self, overwrite=False):
        """Maak een database en vul ze met de demodata.
        Geeft True terug als een bestaande vervangen werd.

        Gooit FileExistsError als de database bestaat en overwrite False is.
        """
        replaced = self.__database.create(overwrite=overwrite)
        Seed(self.__database).import_seed_file()
        return replaced
