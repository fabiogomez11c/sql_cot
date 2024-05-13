from sqlglot.executor import execute
from sqlglot.errors import ExecuteError, OptimizeError
from typing import Dict, Tuple


def execute_query_same_str(answer: str, prediction_query: str, table_dict: Dict) -> Tuple:
    """
    Execute both the correct query and the prediction query and return True if their results are the same
    in a string format.
    """
    try:
        correct = str(execute(answer, tables=table_dict))
    except OptimizeError:
        return False, '', '', "error in correct query, OptimizeError"
    except ExecuteError:
        return False, '', '', "error in correct query, ExecuteError"
    error = ''
    try:
        prediction = str(execute(prediction_query, tables=table_dict))
    except ExecuteError as e:
        error = str(e).split('\n')[0]  # Get only the first line of the error message
        prediction = ''
    except OptimizeError as e:
        error = str(e).split('\n')[0]  # Get only the first line of the error message
        prediction = ''
    return correct == prediction, correct, prediction, error
