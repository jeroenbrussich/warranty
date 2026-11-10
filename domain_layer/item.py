# ./domain_layer/item.py

from dataclasses import dataclass


@dataclass(kw_only=True)
class Item:
    item_id: int | None = None
    item_serial: str | None = None
    item_name: str
    item_make: str
    item_model: str
    item_date_bought: str
    item_warranty: int
    vendor_id: int
