from typing import Dict
from pydantic import BaseModel
from templates import BasePrompt
from langchain_core.language_models.base import BaseLanguageModel
from langchain_core.runnables import RunnableLambda, RunnableParallel
from langchain_replace import RetryOutputParserInvoke


def generate(
    prompt: BasePrompt,
    model: BaseLanguageModel,
    _input: Dict[str, str]
) -> BaseModel:
    """
    Generate a response from the LLM chat and check if the response is valid compared to the
    prompt.parser, if not, try again.
    """
    retry_parser = RetryOutputParserInvoke.from_llm(
        parser=prompt.parser,
        llm=model,
        max_retries=2
    )
    completion_chain = prompt.prompt_template | model
    main_chain = RunnableParallel(
        completion=completion_chain, prompt_value=prompt.prompt_template
    ) | RunnableLambda(lambda x: retry_parser.parse_with_prompt(**x))

    result = main_chain.invoke(_input)
    return result
