# ./data_layer/seed.py
import csv
import sqlite3

import settings
from data_layer.vendor_queries import VendorQueries
from domain_layer.item import Item
from domain_layer.vendor import Vendor


class Seed:
    def __init__(self, database):
        self.__database = database

    def import_seed_file(self):

        connection = self.__database.connect()

        try:
            database_vendor = VendorQueries(connection)
            vendor_ids = {}

            with open(
                settings.SEED_FILE_PATH, "r", encoding="utf-8", newline=""
            ) as seed:
                reader = csv.DictReader(seed)
                for row in reader:
                    new_vendor = Vendor(
                        vendor_name=row["vendor_name"],
                        vendor_url=row["vendor_url"],
                        vendor_is_webshop=row["is_webshop"] == "yes",
                    )

                    key = row["vendor_name"].lower()
                    if key not in vendor_ids:
                        vendor_ids[key] = database_vendor.insert(
                            new_vendor
                        )  # save vendor id

                print(vendor_ids)
        finally:
            connection.close()


if __name__ == "__main__":
    from data_layer.database import Database

    db = Database()
    db.create(overwrite=True)

    seed = Seed(database=db)
    seed.import_seed_file()
