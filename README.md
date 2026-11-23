# Warranty

Een commandline-tool om aankopen en hun garantie bij te houden: wat heb je gekocht, waar, wanneer en hoelang loopt de garantie nog.

## Functionaliteiten

- een item toevoegen, met keuze van de verkoper uit de bestaande verkopers
- een item wijzigen (huidige waarden blijven bewaard met enter)
- een verkoper toevoegen
- een verkoper wijzigen (huidige waarden blijven bewaard met enter; de website wis je met `-`)
- drie lijsten exporteren naar csv: alle items met hun verkoper, enkel de items onder garantie en enkel de items buiten garantie

## Disclaimer

Dit is een demo-app om de werking van Python te verkennen. De ontwikkelaar is zich ervan bewust dat er functionaliteiten ontbreken, en dat het databasemodel hiaten kan vertonen. Dit zijn bewuste keuzes om de POC snel vorm te geven. Mocht de app levensvatbaar zijn, dan kunnen deze tekortkomingen weggewerkt worden.

Roadmap:

- `item_name` (vacuum, car, tv) is eigenlijk een categorie: afsplitsen naar een eigen tabel
- `make` afsplitsen naar eigen tabel
- mogelijkheid toevoegen om items en verkopers te
  - (soft) deleten
- datavalidatie op `seed` implementeren:
  - `is_webshop` moet nu verplicht _yes|no_ zijn
- aankoopprijs bijhouden
- aankoopbewijs bijhouden
- unittests

## App installeren

> [!WARNING]
>
> Deze app heeft minstens Python 3.10 nodig om correct te werken.

### Virtuele omgeving

Voer deze commando's uit in de hoofdmap van het project:

```shell
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # installeert python-dateutil
```

### settings.py

De app werkt niet zonder `settings.py`. Dat bestand zit bewust niet in git. Kopieer het voorbeeld en pas het zo nodig aan:

```shell
cp settings.example.py settings.py
```

| Instelling | Betekenis | Standaard |
| --- | --- | --- |
| `DATA_DIR_NAME` | Naam van de map waarin de database, de demodata en de exports staan | `data` |
| `DATABASE_NAME` | Bestandsnaam van de SQLite-database | `warranty.db` |
| `SEED_FILE_NAME` | Bestandsnaam van de demodata | `demoData.txt` |
| `CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS` | Bestandsnaam van de export met alle items en hun verkoper | `alle_items_met_verkoper.csv` |
| `CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS_UNDER_WARRANTY` | Bestandsnaam van de export met de items onder garantie | `alle_items_met_verkoper_onder_garantie.csv` |
| `CSV_FILE_NAME_ALL_ITEMS_WITH_VENDORS_WARRANTY_EXPIRED` | Bestandsnaam van de export met de items buiten garantie | `alle_items_met_verkoper_garantie_verlopen.csv` |

Onder de lijn "HIERONDER NIETS WIJZIGEN" worden de volledige paden afgeleid (`DATA_DIR`, `DATABASE_PATH`, `SEED_FILE_PATH`). Alle paden zijn relatief aan de plaats van `settings.py`. De app werkt dus ongeacht vanuit welke map je ze start.

## App starten

Voer deze commando's uit in de hoofdmap van het project:

```shell
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m main
```

### De database

De app werkt niet zonder database. Er zijn drie manieren om eraan te komen. Ze worden je aangeboden telkens je de app opstart.

1. **Een bestaande database plaatsen.** Kopieer een bestaande database naar de data-map, met de bestandsnaam uit `DATABASE_NAME`.
2. **Een lege database aanmaken.** Kies bij het opstarten:
    - "een lege database aanmaken" als er nog geen database is, of
    - "vervangen door een lege database" als er al een staat (je krijgt dan eerst een bevestigingsvraag).

    Dit maakt een database met de tabellen uit het schema, zonder rijen.

3. **Een demodatabase aanmaken.** Kies bij het opstarten:
    - "de demo database aanmaken" als er nog geen database is, of
    - "vervangen door de demo database" als er al een staat (je krijgt dan eerst een bevestigingsvraag).

    Dit vult de database met de gegevens uit `demoData.txt`.

Staat er al een database, dan kun je bij het opstarten ook kiezen voor "behouden": de bestaande database blijft dan ongewijzigd.

### De rapporten

Via `lijsten exporteren` in het hoofdmenu schrijf je een lijst weg als csv-bestand in de data-map. Er zijn drie lijsten:

1. alle items met hun verkoper
2. alle items onder garantie (de garantie eindigt vandaag of later)
3. alle items buiten garantie (de garantie is al verlopen)

Elke lijst bevat de gegevens van het item en van de verkoper, aangevuld met de einddatum van de garantie (`item_warranty_end`: de aankoopdatum plus de garantie in maanden). De kolom `vendor_is_webshop` toont `v` voor een webshop en `x` voor een fysieke winkel. De bestandsnaam begint met de datum en het uur van de export (`jjjj_mm_dd_uu_mm_ss_`), gevolgd door de naam uit `settings.py`.

Is er niets om te exporteren, bijvoorbeeld omdat de database leeg is, dan krijg je een melding en wordt er geen bestand gemaakt. Kan het bestand niet worden weggeschreven, dan krijg je ook een melding.

## Bestandsstructuur

```shell
.
├── LICENSE
├── README.md
├── data
│   └── demoData.txt
├── data_layer
│   ├── __init__.py
│   ├── database.py
│   ├── item_queries.py
│   ├── queries.py
│   ├── report_queries.py
│   ├── schema.sql
│   └── vendor_queries.py
├── domain_layer
│   ├── __init__.py
│   ├── item.py
│   └── vendor.py
├── main.py
├── requirements.txt
├── service_layer
│   ├── __init__.py
│   ├── csv_export_service.py
│   ├── database_service.py
│   ├── errors.py
│   ├── item_service.py
│   ├── report_service.py
│   ├── seed.py
│   └── vendor_service.py
├── ui_layer
│   ├── __init__.py
│   ├── helper_functions.py
│   ├── init_application.py
│   ├── items_menu.py
│   ├── main_menu.py
│   ├── reports_menu.py
│   └── vendors_menu.py
└── settings.example.py
```

### main.py

Het ingangspunt van deze applicatie. Controleert bij het opstarten of alle modules en `settings.py` beschikbaar zijn.

### data

Deze map bevat het bestand met de demodata. Demodata is bewust vormgegeven als een niet-genormaliseerd tekstbestand. Het stelt de eerste poging voor van een gebruiker die een garantielijst wilde aanleggen. Dit tekstbestand kan worden ingelezen door `service_layer/seed.py`, dat de data transformeert naar een genormaliseerde databank.

In deze map komt ook de database (`warranty.db`) te staan. Ook de geëxporteerde csv-bestanden komen hier terecht. Die zitten niet in git.

### data_layer

Deze map bevat alle code die met SQLite praat:

- `database.py`: de klasse `Database`, die connecties opent (met foreign keys aan) en de database aanmaakt.
- `schema.sql`: de `CREATE TABLE`-statements.
- `queries.py`: een kleine helper klasse die de queries uitvoert; `ItemQueries`, `VendorQueries` en `ReportQueries` erven ervan
- `item_queries.py`: verzameling van alle queries voor de tabel `item`
- `vendor_queries.py`: verzameling van alle queries voor de tabel `vendor`
- `report_queries.py`: de query voor de rapporten: alle items samen met hun verkoper

### domain_layer

Deze map bevat de domeinklassen, oftewel de objecten waarover de applicatie gaat:

- `Item`
- `Vendor`

### service_layer

Deze map bevat de complexe businesslogica, of klassen die data transformeren voor opslag of output.

- `database_service.py`: de klasse `DatabaseService`, die nagaat of de database bestaat en een lege database of een demodatabase aanmaakt (de demodata wordt ingelezen via `Seed`).
- `errors.py`: de uitzonderingen `StorageError`, die de services gooien als iets in de database mislukt, anders dan een dubbele waarde, `NoDataToExportError` als er geen rijen zijn om te exporteren en `ExportError` als het csv-bestand niet kan worden weggeschreven.
- `seed.py` leest het demobestand `SEED_FILE_NAME` (standaard data/demoData.txt) uit en transformeert de data zodat die naar de database kan worden weggeschreven.
- `item_service.py`: de klasse `ItemService`, die  `Item`s toevoegt, wijzigt en opvraagt. Bij een dubbel serienummer gooit ze een `DuplicateSerialError`. Andere databasefouten worden een `StorageError`.
- `vendor_service.py`: de klasse `VendorService`, die `Vendor`s toevoegt, wijzigt en opvraagt. Bij een dubbele verkopersnaam (hoofdletterongevoelig) gooit ze een `DuplicateVendorNameError`. Andere databasefouten worden een `StorageError`.
- `report_service.py`: de klasse `ReportService`, die de items met hun verkoper opvraagt, de einddatum van de garantie berekent (aankoopdatum plus garantie in maanden), de lijst eventueel filtert op onder of buiten garantie en doorgeeft aan `csv_export_service.py`. Databasefouten worden een `StorageError`.
- `csv_export_service.py`: schrijft een lijst rijen weg naar een csv-bestand in de data-map, met de datum en het uur van de export voor de bestandsnaam. Geeft het pad van het bestand terug.

### ui_layer

Deze map bevat de functies die de interface vormen tussen gebruiker en applicatie. De menu's krijgen hun services van `main.py`. Fouten van de services (`DuplicateSerialError`, `DuplicateVendorNameError`, `StorageError`, `NoDataToExportError` en `ExportError`) worden opgevangen en als melding getoond.

- `helper_functions.py`: een collectie van generieke functies die op meerdere plaatsen gebruikt kunnen worden: een bevestiging of keuze vragen, tekst, een datum (`dd-mm-jjjj`) of een garantie in maanden inlezen, en een verkoper of item kiezen. Elke functie blijft vragen tot de invoer geldig is. Bij het wijzigen krijgen de vragen een standaardwaarde mee, die met enter behouden blijft.
- `init_application.py`: het menu dat bij het opstarten verschijnt. Je kiest of je een lege database aanmaakt, de demo-database aanmaakt, of een bestaande database behoudt. Wil je een bestaande database vervangen, dan vraagt het menu eerst om bevestiging.
- `main_menu.py`: toont het hoofdmenu met de opties `items beheren`, `verkopers beheren`, `lijsten exporteren` en `de app sluiten`.
- `items_menu.py`: het menu voor items. Hier kun je een item toevoegen of wijzigen. Je kiest eerst de verkoper (of annuleert) en vult daarna de overige gegevens in. Bij het wijzigen toont elke vraag de huidige waarde, en met enter behoud je die. Een serienummer wis je door - in te typen.
- `reports_menu.py`: het menu voor de rapporten. Je kiest welke lijst je wilt exporteren en krijgt het pad van het weggeschreven csv-bestand te zien.
- `vendors_menu.py`: het menu voor verkopers. Hier kun je een verkoper toevoegen of wijzigen. De website is optioneel: bij het toevoegen laat je ze leeg, bij het wijzigen wis je ze door - in te typen. Bestaat de naam al (hoofdletters tellen niet), dan toont het menu een melding en wordt niets opgeslagen.

## Database

```dbml
Table item {
  item_id integer [pk]
  item_serial varchar [unique, null, note: 'optioneel; meerdere items zonder serienummer mogen']
  item_name varchar [not null]
  item_make varchar [not null]
  item_model varchar [not null]
  vendor_id integer [not null, ref: > vendor.vendor_id]
  item_date_bought date [not null, note: 'ISO-formaat, bv. 2025-10-10']
  item_warranty integer [not null, note: 'in maanden, minstens 0 (CHECK in schema.sql)']
}

Table vendor {
  vendor_id integer [pk]
  vendor_name varchar [not null, unique, note: 'hoofdletterongevoelig']
  vendor_url varchar [null, note: 'optioneel']
  vendor_is_webshop bool [not null, note: 'in SQLite 0 of 1 (CHECK in schema.sql)']
}
```

`data_layer/schema.sql` is de bron van waarheid voor wat de database echt afdwingt (`CHECK`, `COLLATE NOCASE`). DBML kent die niet.
