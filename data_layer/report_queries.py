# ./data_layer/report_queries.py

from data_layer.queries import Queries


class ReportQueries(Queries):
    def get_items_with_vendors(self):
        query = """
            SELECT
                item.item_id,
                item.item_serial,
                item.item_name,
                item.item_make,
                item.item_model,
                item.item_date_bought,
                item.item_warranty,
                vendor.vendor_id,
                vendor.vendor_name,
                vendor.vendor_url,
                vendor.vendor_is_webshop
            FROM item
                JOIN vendor ON item.vendor_id = vendor.vendor_id
            ORDER BY item.item_id
        """
        cursor = self._execute(query)

        rows = cursor.fetchall()

        results = []
        for row in rows:
            item = {
                "item_id": row[0],
                "item_serial": row[1],
                "item_name": row[2],
                "item_make": row[3],
                "item_model": row[4],
                "item_date_bought": row[5],
                "item_warranty_months": row[6],
                "vendor_id": row[7],
                "vendor_name": row[8],
                "vendor_url": row[9] or None,
                "vendor_is_webshop": bool(row[10]),
            }
            results.append(item)

        return results
