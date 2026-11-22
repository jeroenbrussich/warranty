# ./service_layer/report_service.py

import sqlite3
from datetime import date, datetime

from dateutil.relativedelta import relativedelta

import service_layer.csv_export_service as exporter
import settings
from data_layer.report_queries import ReportQueries
from service_layer.errors import StorageError


class ReportService:
    def __init__(self, database):
        self.__database = database

    def export_items_with_vendors(self):
        rows = self.__get_items_with_vendor_and_warranty_end_date()
        return exporter.write_rows_to_csv(
            rows=rows, filename=settings.CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS
        )

    def export_items_under_warranty(self):
        under_warranty = lambda item: (
            datetime.strptime(item["item_warranty_end"], "%Y-%m-%d").date()
            >= date.today()
        )
        rows = self.__get_items_with_vendor_and_warranty_end_date()
        return exporter.write_rows_to_csv(
            rows=list(filter(under_warranty, rows)),
            filename=settings.CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS_UNDER_WARRANTY,
        )

    def export_items_out_of_warranty(self):
        warranty_expired = lambda item: (
            datetime.strptime(item["item_warranty_end"], "%Y-%m-%d").date()
            < date.today()
        )
        rows = self.__get_items_with_vendor_and_warranty_end_date()
        return exporter.write_rows_to_csv(
            rows=list(filter(warranty_expired, rows)),
            filename=settings.CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS_WARRANTY_EXPIRED,
        )

    def __get_items_with_vendor_and_warranty_end_date(self):
        connection = self.__database.connect()
        try:
            rows = ReportQueries(connection).get_items_with_vendors()
        except sqlite3.DatabaseError as err:
            raise StorageError(str(err)) from err
        finally:
            connection.close()

        for row in rows:
            warranty_end_date = self.__calculate_end_date(
                row["item_date_bought"], row["item_warranty_months"]
            )
            warranty_end = datetime.strftime(warranty_end_date, "%Y-%m-%d")
            row["item_warranty_end"] = warranty_end
            row["vendor_is_webshop"] = "v" if row["vendor_is_webshop"] else "x"

        return rows

    def __calculate_end_date(self, date_bought, months):
        start = datetime.strptime(date_bought, "%Y-%m-%d").date()
        return start + relativedelta(months=months)
