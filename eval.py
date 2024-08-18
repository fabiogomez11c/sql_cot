import sqlite3


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

    def evaluate_query(self, query: str, gold_query: str, database: str) -> bool:
        """
        Evaluates with Exact Match metric the query with respect to the
        gold query given the database
        """
        query_result = self._execute_query(query, database)
        gold_result = self._execute_query(gold_query, database)

        return query_result == gold_result
