# ./service_layer/vendor_service.py

from data_layer.vendor_queries import VendorQueries


class VendorService:
    def __init__(self, database):
        self.__database = database

    def get_all_vendors(self):
        connection = self.__database.connect()
        try:
            return VendorQueries(connection).get_all()
        finally:
            connection.close()
