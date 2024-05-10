from pydantic import BaseModel, Field
from langchain_together import ChatTogether
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_community.utils.openai_functions import convert_pydantic_to_openai_function

model = ChatTogether(model="mistralai/Mixtral-8x7B-Instruct-v0.1")


class SQLQuery(BaseModel):
    query: str = Field(..., description='SQL query to answer the question')


query = "Create a sample SQL query to answer the question: What is the average age of users?"

parser = JsonOutputParser(pydantic_object=SQLQuery)
prompt = PromptTemplate(
    template="Answer the question:{question} with the format: {format_instructions}",
    input_variables=["question"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

res = prompt | model | parser
result = res.invoke({"question": query})
print(result)
