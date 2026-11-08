CREATE TABLE IF NOT EXISTS vendor (
    vendor_id INTEGER PRIMARY KEY,
    vendor_name TEXT NOT NULL UNIQUE COLLATE NOCASE,
    vendor_url TEXT NOT NULL,
    vendor_is_webshop INTEGER NOT NULL CHECK (vendor_is_webshop IN (0, 1)) -- 0 = fysieke winkel, 1 = webshop
);


CREATE TABLE IF NOT EXISTS item (
    item_id INTEGER PRIMARY KEY,
    item_serial TEXT UNIQUE NULL,
    item_name TEXT NOT NULL,
    item_make TEXT NOT NULL,
    item_model TEXT NOT NULL,
    vendor_id INTEGER NOT NULL,
    item_date_bought DATE NOT NULL,
    item_warranty INTEGER NOT NULL, -- in months
    FOREIGN KEY(vendor_id) REFERENCES vendor(vendor_id),
    CHECK (item_warranty >= 0)
);