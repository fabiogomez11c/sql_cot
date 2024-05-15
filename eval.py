from sqlglot.executor import execute
from sqlglot.errors import ExecuteError, OptimizeError
from typing import Dict, Tuple, List
from pydantic_models import LLMEval
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain.prompts import PromptTemplate
from time import sleep


def execute_query_same_str(answer: str, prediction_query: str, table_dict: Dict) -> Tuple:
    """
    Execute both the correct query and the prediction query and return True if their results are the same
    in a string format.
    """
    try:
        correct = execute(answer, tables=table_dict)
    except OptimizeError:
        return False, '', '', "error in correct query, OptimizeError"
    except ExecuteError:
        return False, '', '', "error in correct query, ExecuteError"
    error = ''
    try:
        prediction = execute(prediction_query, tables=table_dict)
    except ExecuteError as e:
        error = str(e).split('\n')[0]  # Get only the first line of the error message
        prediction = ''
    except OptimizeError as e:
        error = str(e).split('\n')[0]  # Get only the first line of the error message
        prediction = ''
    return correct.rows == prediction.rows, str(correct), str(prediction), error


def evaluate_with_llm(answer: str, prediction_query: str, context: str, question: str) -> List:
    """
    Use an LLM to evaluate if the prediction_query, the answer or both can solve the question
    given the context.
    """
    votes = []
    for _ in range(3):
        try:
            llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.0)
            parser = JsonOutputParser(pydantic_object=LLMEval)
            prompt = PromptTemplate(
                template="{format_instructions}\nGiven 3 options, select which of them is true according to the context and the question, select which of the queries do a better job at solving the question, if both queries solve the question select option C.\nContext:{context}\nQuestion:{question}\nA:{A}\nB:{B}\nC:Both A and B solve the question.",  # noqa
                input_variables=["context", "question", "A", "B"],
                partial_variables={'format_instructions': parser.get_format_instructions()}
            )
            chain = prompt | llm | parser
            response = chain.invoke({"context": context, "question": question, "A": answer, "B": prediction_query})
            votes.append(response['choice'])
        except Exception as e:  # noqa
            raise Exception("Error in LLM")
        sleep(0.5)
    return votes
