# README

## Disclaimer

Dit is een demo-app om de werking van Python te verkennen. De ontwikkelaar is zich ervan bewust dat er functionaliteiten ontbreken, en dat het databasemodel hiaten kan vertonen. Dit zijn bewuste keuzes om de POC snel vorm te geven. Mocht de app levensvatbaar zijn, dan kunnen deze tekortkomingen weggewerkt worden.

## filestructure

```shell
.
├── LICENSE
├── README.md
├── data
│   └── demoData.txt
├── data_layer
│   └── __init__.py
└── main.py
```

### data

Deze map bevat het bestand met de demodata. Demodata is bewust vormgegeven als een niet genormaliseerd tekstbestand. Het stelt de eerste poging voor van een gebruiker die een garantielijst wilde aanleggen. Dit tekstbestand kan worden ingelezen door `data_layer/seed.py`, dat de data transformeert naar een genormaliseerde databank.

In deze map zal ook de database (warranty.db) komen te staan.

### data_layer

Deze map bevat de database-package die met de sqlite3-database praat.

## database

```dbml

Table item {
  item_id integer [pk]
  item_serial varchar [unique, null]
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
