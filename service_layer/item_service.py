# ./service_layer/item_service.py

import sqlite3

from data_layer.item_queries import ItemQueries


class DuplicateSerialError(Exception):
    pass


class ItemService:
    def __init__(self, database):
        self.__database = database

    def add_item(self, item):
        connection = self.__database.connect()
        try:
            return ItemQueries(connection).insert(
                item
            )  # returns id of the inserted item
        except sqlite3.IntegrityError as err:
            if "item_serial" in str(err):
                raise DuplicateSerialError(item.item_serial) from err
            raise
        finally:
            connection.close()
