# ./data_layer/vendor_queries.py

from data_layer.queries import Queries
from domain_layer.vendor import Vendor


class VendorQueries(Queries):
    def insert(self, vendor):
        query = """
                INSERT INTO vendor(vendor_name, vendor_url, vendor_is_webshop)
                VALUES(?, ?, ?)
            """
        cursor = self._execute(
            query, (vendor.vendor_name, vendor.vendor_url, vendor.vendor_is_webshop)
        )
        return cursor.lastrowid

    def get_all(self):
        query = """
            SELECT 
                vendor_id,
                vendor_name,
                vendor_url,
                vendor_is_webshop
            FROM vendor 
            ORDER BY vendor_id
        """

        cursor = self._execute(query)
        rows = cursor.fetchall()

        results = []
        for vendor_id, name, url, is_webshop in rows:
            results.append(
                Vendor(
                    vendor_id=vendor_id,
                    vendor_name=name,
                    vendor_url=url,
                    vendor_is_webshop=bool(is_webshop),
                )
            )
        return results
