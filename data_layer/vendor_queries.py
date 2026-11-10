# ./data_layer/vendor_queries.py
import sqlite3


class VendorQueries:
    def __init__(self, connection: sqlite3.Connection):
        self.__connection = connection

    def insert(self, vendor):
        connection = self.__connection
        sql = """
                INSERT INTO vendor(vendor_name, vendor_url, vendor_is_webshop)
                VALUES(?, ?, ?)
            """
        cursor = connection.execute(
            sql, (vendor.vendor_name, vendor.vendor_url, vendor.vendor_is_webshop)
        )
        connection.commit()
        return cursor.lastrowid
