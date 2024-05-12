from langchain.output_parsers import RetryOutputParser
from langchain_core.exceptions import OutputParserException
from langchain_core.prompt_values import PromptValue
from langchain_core.messages import AIMessage
from typing import TypeVar

T = TypeVar("T")


class RetryOutputParserInvoke(RetryOutputParser):

    def parse_with_prompt(self, completion: AIMessage, prompt_value: PromptValue) -> T:
        """Parse the output of an LLM call using a wrapped parser.

        Args:
            completion: The chain completion to parse.
            prompt_value: The prompt to use to parse the completion.

        Returns:
            The parsed completion.
        """
        retries = 0

        while retries <= self.max_retries:
            try:
                # aim for ChatGeneration and not for Generation, see output_parsers.base.BaseOutputParser.invoke
                return self.parser.invoke(completion)
            except OutputParserException as e:
                if retries == self.max_retries:
                    raise e
                else:
                    retries += 1
                    completion = self.retry_chain.run(
                        prompt=prompt_value.to_string(), completion=completion.content
                    )

        raise OutputParserException("Failed to parse")
