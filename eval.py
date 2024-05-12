from sqlglot.executor import execute
from typing import Dict


def execute_query_same_str(answer: str, prediction_query: str, table_dict: Dict) -> bool:
    """
    Execute both the correct query and the prediction query and return True if their results are the same
    in a string format.
    """
    correct = str(execute(answer, tables=table_dict))
    prediction = str(execute(prediction_query, tables=table_dict))
    return correct == prediction
