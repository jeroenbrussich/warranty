# ./service_layer/csv_export_layer.py
import csv
import os
from datetime import datetime

import settings


def write_rows_to_csv(rows, filename):
    if not filename or not filename.strip():
        raise ValueError("Filename mag niet None zijn.")

    if not len(rows):
        raise ValueError("Ik heb geen data om te exporteren.")

    prefix = datetime.strftime(datetime.now(), "%Y_%m_%d_%H_%M_%S_")
    headers = list(rows[0].keys())
    filepath = os.path.join(settings.DATA_DIR, prefix + filename)

    if not filepath.endswith(".csv"):
        filename += ".csv"

    os.makedirs(settings.DATA_DIR, exist_ok=True)

    with open(filepath, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    return filepath
