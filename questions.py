from typing import List
from pydantic import BaseModel, Field
import json


class Question(BaseModel):
    question: str = Field(..., description="question to be answered")
    db_id: str = Field(..., description="database to use")


class SetQuestions(BaseModel):
    set_questions: List[Question]


def read_json_file_with_questions(file_path: str) -> SetQuestions:
    """
    Read json file with the information needed to build the SetQuestions
    """
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    questions = [Question(question=q["question"], db_id=q["db_id"]) for q in data]
    return SetQuestions(set_questions=questions)
