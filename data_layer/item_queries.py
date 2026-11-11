# ./data_layer/vendor_queries.py
from data_layer.queries import Queries


class ItemQueries(Queries):
    def insert(self, item):
        sql = """
                INSERT INTO item(item_serial, item_name, item_make, item_model, vendor_id, item_date_bought, item_warranty)
                VALUES(?, ?, ?, ?, ?, ?, ?)
            """
        cursor = self._execute(
            sql,
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
