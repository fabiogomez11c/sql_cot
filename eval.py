import sqlite3
from IPython import embed as ipython


class ExactMatch:

    def _connect(self, database: str):
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(database)

        # Create a cursor object
        return conn.cursor()

    def _execute_query(self, query: str, database: str) -> str:
        """
        This method is aimed to only use queries that do not modify the database.
        """
        # create connectioncursor =
        cursor = self._connect(database=database)
        # execute query
        cursor.execute(query)
        query_result = cursor.fetchone()
        return query_result
