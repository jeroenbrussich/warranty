# ./data_layer/seed.py
import csv
from datetime import datetime

import settings
from data_layer.item_queries import ItemQueries
from data_layer.vendor_queries import VendorQueries
from domain_layer.item import Item
from domain_layer.vendor import Vendor


class Seed:
    def __init__(self, database):
        self.__database = database

    def import_seed_file(self):

        connection = self.__database.connect()

        try:
            vendor_queries = VendorQueries(connection)
            item_queries = ItemQueries(connection)
            vendor_ids = {}

            with open(
                settings.SEED_FILE_PATH, "r", encoding="utf-8", newline=""
            ) as seed:
                reader = csv.DictReader(seed)
                for row in reader:
                    key = row["vendor_name"].lower()

                    if key not in vendor_ids:
                        vendor_ids[key] = vendor_queries.insert(
                            Vendor(
                                vendor_name=row["vendor_name"],
                                vendor_url=row["vendor_url"],
                                vendor_is_webshop=row["is_webshop"] == "yes",
                            )
                        )  # store vendor id

                    item_queries.insert(
                        Item(
                            item_serial=row["serial_number"] or None,
                            item_name=row["item"],
                            item_make=row["make"],
                            item_model=row["model"],
                            item_date_bought=row["date_bought"],
                            item_warranty=self.__months_between_dates(
                                row["date_bought"], row["warranty_end"]
                            ),
                            vendor_id=vendor_ids[key],
                        )
                    )
        finally:
            connection.close()

    def __months_between_dates(self, start_date, end_date):
        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()

        years = end.year - start.year
        months = end.month - start.month

        return years * 12 + months
