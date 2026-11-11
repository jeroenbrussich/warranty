# ./data_layer/vendor_queries.py
from data_layer.queries import Queries


class VendorQueries(Queries):
    def insert(self, vendor):
        sql = """
                INSERT INTO vendor(vendor_name, vendor_url, vendor_is_webshop)
                VALUES(?, ?, ?)
            """
        cursor = self._execute(
            sql, (vendor.vendor_name, vendor.vendor_url, vendor.vendor_is_webshop)
        )
        return cursor.lastrowid
