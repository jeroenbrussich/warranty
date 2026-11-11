# ./data_layer/queries.py
import sqlite3


class Queries:
    def __init__(self, connection: sqlite3.Connection):
        self._connection = connection

    def _execute(self, sql, parameters=()):
        cursor = self._connection.execute(sql, parameters)
        self._connection.commit()
        return cursor
