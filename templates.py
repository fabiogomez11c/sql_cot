from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser  # noqa
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List


class BasePrompt:
    template: str
    input_variables: List[str]

    def __init__(self, pydantic_model: BaseModel):
        self.pydantic_model = pydantic_model
        self.parser = PydanticOutputParser(pydantic_object=pydantic_model)
        self.prompt_template = PromptTemplate(
            template=self.template,
            input_variables=self.input_variables,
            partial_variables={'format_instructions': self.parser.get_format_instructions()}
        )


class DummyTable(BasePrompt):
    template: str = "Generate a dummy table with 5 rows that corresponds to:\n{user_context}\nThat could answer a question like:\n{user_question}\nWith the following format:\n{format_instructions}"  # noqa
    input_variables: List[str] = ['user_context', 'user_question']

    def __init__(self, pydantic_model: BaseModel):
        super().__init__(pydantic_model)


class SQLPrompt(BasePrompt):
    template: str = "Answer the question with the format:\n{format_instructions}\nGive me a query that could answer the question: {user_input}?\nContext table: {context_table}"  # noqa
    input_variables: List[str] = ['user_input', 'context_table']

    def __init__(self, pydantic_model: BaseModel):
        super().__init__(pydantic_model)
