from pydantic import BaseModel, Field
from langchain_together import ChatTogether
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser
from langchain_community.utils.openai_functions import convert_pydantic_to_openai_function

model = ChatTogether(model="mistralai/Mixtral-8x7B-Instruct-v0.1", temperature=0.0)


class SQLQuery(BaseModel):
    query: str = Field(..., description='SQL query to answer the question')


query = "Create a sample SQL query to answer the question: What is the average age of users?"

prompt = PromptTemplate(
    template="Answer the question: {question}",
    input_variables=["question"]
)
parser = JsonOutputFunctionsParser()
openai_functions = [convert_pydantic_to_openai_function(SQLQuery)]

res = prompt | model.bind(functions=openai_functions) | parser
res.invoke({"question": query})
print(res)
