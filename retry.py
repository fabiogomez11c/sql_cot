"""Script to test the retry parser from langchain"""
from langchain.output_parsers import RetryOutputParser
from langchain.output_parsers import OutputFixingParser
from langchain.output_parsers import PydanticOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI, OpenAI

template = """Based on the user question, provide an Action and Action Input for what step should be taken.
{format_instructions}
Question: {query}
Response:"""


class Action(BaseModel):
    action: str = Field(..., description="action to take")
    action_input: str = Field(..., description="input to the action")


parser = PydanticOutputParser(pydantic_object=Action)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

prompt_value = prompt.format_prompt(query="whois lei do caprios gf")

bad_response = '{"action": "search"}'

# parser.parse(bad_response)

# fix_parser = OutputFixingParser.from_llm(parser=parser, llm=OpenAI())
# fix_parser.parse(bad_response)


retry_parser = RetryOutputParser.from_llm(parser=parser, llm=OpenAI(temperature=0), max_retries=1)
result = retry_parser.parse_with_prompt(bad_response, prompt_value)
print(result)
