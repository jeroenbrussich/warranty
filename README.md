# Warranty

Een commandline-tool om aankopen en hun garantie bij te houden: wat heb je gekocht, waar, wanneer en hoelang loopt de garantie nog.

> Functionaliteiten: TODO (invullen zodra het menu bestaat)

## Disclaimer

Dit is een demo-app om de werking van Python te verkennen. De ontwikkelaar is zich ervan bewust dat er functionaliteiten ontbreken, en dat het databasemodel hiaten kan vertonen. Dit zijn bewuste keuzes om de POC snel vorm te geven. Mocht de app levensvatbaar zijn, dan kunnen deze tekortkomingen weggewerkt worden.

## App installeren

### Virtuele omgeving

Voer deze commando's uit in de hoofdmap van het project:

```shell
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt  # TODO: requirements.txt bestaat nog niet
```

### settings.py

De app werkt niet zonder `settings.py`. Dat bestand zit bewust niet in git. Kopieer het voorbeeld en pas het zo nodig aan:

```shell
cp settings.example.py settings.py
```

| Instelling | Betekenis | Standaard |
| --- | --- | --- |
| `DATA_DIR_NAME` | Naam van de map waarin de database en demodata staan | `data` |
| `DATABASE_NAME` | Bestandsnaam van de SQLite-database | `warranty.db` |
| `SEED_FILE_NAME` | Bestandsnaam van de demodata | `demoData.txt` |

Onder de lijn "HIERONDER NIETS WIJZIGEN" worden de volledige paden afgeleid (`DATA_DIR`, `DATABASE_PATH`, `SEED_FILE_PATH`). Alle paden zijn relatief aan de plaats van `settings.py`. De app werkt dus ongeacht vanuit welke map je ze start.

### De database

De app werkt niet zonder database. Er zijn drie manieren om eraan te komen. Start de app vanuit de hoofdmap met `python main.py`.

1. **Een bestaande database plaatsen.** Kopieer een bestaande database naar de data-map, met de bestandsnaam uit `DATABASE_NAME`.
2. **Een lege database aanmaken.** Kies bij het opstarten:
    - "een lege database aanmaken" als er nog geen database is, of
    - "vervangen door een lege database" als er al een staat (je krijgt dan eerst een bevestigingsvraag).

    Dit maakt een database met de tabellen uit het schema, zonder rijen.

3. **Een demodatabase aanmaken.** Kies bij het opstarten:
    - "de demo database aanmaken" als er nog geen database is, of
    - "vervangen door de demo database" als er al een staat.

    Dit vult de database met de gegevens uit `demoData.txt`. TODO: werkt pas als `data_layer/seed.py` bestaat.

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
│   └── schema.sql
├── main.py
└── settings.example.py
```

### data

Deze map bevat het bestand met de demodata. Demodata is bewust vormgegeven als een niet-genormaliseerd tekstbestand. Het stelt de eerste poging voor van een gebruiker die een garantielijst wilde aanleggen. Dit tekstbestand kan worden ingelezen door `data_layer/seed.py`, dat de data transformeert naar een genormaliseerde databank.

In deze map komt ook de database (`warranty.db`) te staan. Die zit niet in git.

### data_layer

Deze map bevat alle code die met SQLite praat:

- `database.py`: de klasse `Database`, die connecties opent (met foreign keys aan) en de database aanmaakt.
- `schema.sql`: de `CREATE TABLE`-statements.

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
  vendor_url varchar [not null]
  vendor_is_webshop bool [not null, note: 'in SQLite 0 of 1 (CHECK in schema.sql)']
}
```

`data_layer/schema.sql` is de bron van waarheid voor wat de database echt afdwingt (`CHECK`, `COLLATE NOCASE`). DBML kent die niet.
