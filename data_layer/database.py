# ./data_layer/database.py
import os
import sqlite3

import settings

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")


class Database:
    def __init__(self, path=settings.DATABASE_PATH):
        self.path = path

    def exists(self):
        return os.path.isfile(self.path)

    def connect(self):
        connection = sqlite3.connect(self.path)
        connection.execute("PRAGMA foreign_keys = ON")
        return connection

    def create(self, overwrite=False):
        """Maak de database aan. Geeft True terug als een bestaande vervangen werd.

        Gooit FileExistsError als de database bestaat en overwrite False is.
        """
        database_already_exists = self.exists()

        with open(SCHEMA_PATH, encoding="utf-8") as schema:
            sql_schema = schema.read()

        if not overwrite and database_already_exists:
            raise FileExistsError(self.path)

        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        if overwrite and database_already_exists:
            os.remove(self.path)

        connection = self.connect()
        try:
            connection.executescript(sql_schema)
        except sqlite3.Error:
            connection.close()
            os.remove(self.path)
            raise
        connection.close()

        return database_already_exists
