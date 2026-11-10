# ./domain_layer/vendor.py

from dataclasses import dataclass


@dataclass(kw_only=True)
class Vendor:
    vendor_id: int | None = None
    vendor_name: str
    vendor_url: str
    vendor_is_webshop: bool
