# ./service_layer/vendor_service.py

import sqlite3

from data_layer.vendor_queries import VendorQueries


class DuplicateVendorNameError(Exception):
    pass


class VendorService:
    def __init__(self, database):
        self.__database = database

    def add_vendor(self, vendor):
        connection = self.__database.connect()
        try:
            return VendorQueries(connection).insert(vendor)
        except sqlite3.IntegrityError as err:
            if "vendor_name" in str(err):
                raise DuplicateVendorNameError(vendor.vendor_name) from err
            raise
        finally:
            connection.close()

    def update_vendor(self, vendor):
        connection = self.__database.connect()
        try:
            return VendorQueries(connection).update(vendor)
        except sqlite3.IntegrityError as err:
            if "vendor_name" in str(err):
                raise DuplicateVendorNameError(vendor.vendor_name) from err
            raise
        finally:
            connection.close()

    def get_all_vendors(self):
        connection = self.__database.connect()
        try:
            return VendorQueries(connection).get_all()
        finally:
            connection.close()
