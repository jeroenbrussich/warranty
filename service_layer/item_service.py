# ./service_layer/item_service.py

from data_layer.item_queries import ItemQueries


class ItemService:
    def __init__(self, database):
        self.__database = database

    def add_item(self, item):
        connection = self.__database.connect()
        try:
            return ItemQueries(connection).insert(
                item
            )  # returns id of the inserted item
        finally:
            connection.close()
