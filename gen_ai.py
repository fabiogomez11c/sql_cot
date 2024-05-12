from pydantic import BaseModel
from templates import BasePrompt
from langchain_openai.chat_models.base import BaseChatOpenAI
from langchain_core.exceptions import OutputParserException
from langchain.output_parsers import RetryOutputParser
from langchain_openai import OpenAI
from typing import Dict


def generate(
    prompt: BasePrompt,
    model: BaseChatOpenAI,
    _input: Dict[str, str]
) -> BaseModel:
    try:
        chain = prompt.prompt_template | model | prompt.parser
        response = chain.invoke(_input)
    except OutputParserException:  # retry in case of outputparser error
        retry_parser = RetryOutputParser.from_llm(
            llm=OpenAI(temperature=0),  # default model is: gpt-3.5-turbo-instruct
            parser=prompt.parser,
            max_retries=2
        )
        response = retry_parser.parse_with_prompt(
            completion=response,
            prompt_value=prompt.prompt_template.format_prompt(**_input),
        )
    return response
