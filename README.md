# README

## filestructure

```shell
.
├── README.md
├── data
├── data_layer
│   └── __init__.py
└── main.py
```

### data

Deze map bevat de database.

### data_layer

Deze map bevat de database-package die met de sqlite3-database praat.

## database

```dbml

Table item {
  item_id integer [pk]
  item_name varchar [not null]
  item_make varchar [not null]
  item_model varchar [not null]
  vendor_id integer [not null, ref: > vendor.vendor_id]
  item_date_bought date [not null]
  item_warranty integer [not null] // in months
}

Table vendor {
  vendor_id integer [pk]
  vendor_name varchar [not null]
  vendor_url varchar [not null]
  vendor_is_webshop bool [not null]
}

```
