import unittest
import sqlite3
from eval import ExactMatch  # Replace 'your_module' with the actual module name
from IPython import embed as ipython


class TestExactMatch(unittest.TestCase):
    def setUp(self):
        self.exact_match = ExactMatch()
        self.database = "./spider/database/activity_1/activity_1.sqlite"

    def test_connect(self):
        cursor = self.exact_match._connect(self.database)
        self.assertIsInstance(cursor, sqlite3.Cursor)

    def test_execute_query(self):
        query = "SELECT COUNT(*) FROM Activity"
        result = self.exact_match._execute_query(query, self.database)
        self.assertIsNotNone(result)
        self.assertIsInstance(result[0], int)

    def test_execute_query_with_data(self):
        query = "SELECT * FROM Activity LIMIT 1"
        result = self.exact_match._execute_query(query, self.database)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)

    def test_execute_query_no_results(self):
        query = "SELECT * FROM Activity WHERE actid = -1"
        result = self.exact_match._execute_query(query, self.database)
        self.assertIsNone(result)

    def test_activity_count(self):
        query = "SELECT COUNT(*) FROM Activity"
        result = self.exact_match._execute_query(query, self.database)
        self.assertEqual(result[0], 16)


if __name__ == "__main__":
    unittest.main()
