from templates import BasePrompt
from langchain_openai.chat_models.base import BaseChatOpenAI
from typing import Dict


def generate(
    prompt: BasePrompt,
    model: BaseChatOpenAI,
    _input: Dict[str, str]
) -> Dict:
    chain = prompt.prompt_template | model | prompt.parser
    response = chain.invoke(_input)
    return response
