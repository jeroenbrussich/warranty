# ./data_layer/item_queries.py

from data_layer.queries import Queries
from domain_layer.item import Item


class ItemQueries(Queries):
    def insert(self, item):
        query = """
                INSERT INTO item(item_serial, item_name, item_make, item_model, vendor_id, item_date_bought, item_warranty)
                VALUES(?, ?, ?, ?, ?, ?, ?)
            """
        cursor = self._execute(
            query,
            (
                item.item_serial,
                item.item_name,
                item.item_make,
                item.item_model,
                item.vendor_id,
                item.item_date_bought,
                item.item_warranty,
            ),
        )
        return cursor.lastrowid

    def get_all(self):
        query = """
                SELECT
                    item_id,
                    item_serial,
                    item_name,
                    item_make,
                    item_model,
                    item_date_bought,
                    item_warranty,
                    vendor_id
                FROM item
                ORDER BY item_id
            """

        cursor = self._execute(query)
        rows = cursor.fetchall()

        results = []
        for (
            item_id,
            serial,
            name,
            make,
            model,
            date_bought,
            warranty,
            vendor_id,
        ) in rows:
            results.append(
                Item(
                    item_id=item_id,
                    item_serial=serial,
                    item_name=name,
                    item_make=make,
                    item_model=model,
                    item_date_bought=date_bought,
                    item_warranty=warranty,
                    vendor_id=vendor_id,
                )
            )

        return results

    def update(self, item):
        query = """
                UPDATE item
                SET
                    item_serial = ?,
                    item_name = ?,
                    item_make = ?,
                    item_model = ?,
                    item_date_bought= ?,
                    item_warranty = ?,
                    vendor_id = ?
                WHERE item_id = ?
            """
        self._execute(
            query,
            (
                item.item_serial,
                item.item_name,
                item.item_make,
                item.item_model,
                item.item_date_bought,
                item.item_warranty,
                item.vendor_id,
                item.item_id,
            ),
        )
        return item.item_id
