from pydantic_models import SQLQuery
from langchain_together import ChatTogether  # noqa
from langchain_openai.chat_models import ChatOpenAI  # noqa
from utils import load_prepare_dev_dataset, store_results  # noqa
from gen_ai import generate
from evaluation import evaluate
from templates import SQLPrompt
from tqdm import tqdm
import pandas as pd

reference = ''
temperature = 0.0
# model_name = "meta-llama/Llama-3-70b-chat-hf"
model_name = "gpt-3.5-turbo-0125"
# model_name = "meta-llama/Llama-2-70b-chat-hf"
# model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
# model_name = "togethercomputer/CodeLlama-34b-Instruct"
# model = ChatTogether(
#     model=model_name,
#     temperature=temperature
# )
model = ChatOpenAI(model=model_name, temperature=0.0)

print('Downloading the data')
data = load_prepare_dev_dataset()[:300]

results = []
result_queries = []
gold_queries = []
correct_count = 0
correct_error = 0
progress_bar = tqdm(data, total=len(data))
for instance in progress_bar:
    try:
        result = generate(
            prompt=SQLPrompt(pydantic_model=SQLQuery),
            model=model,
            _input={'user_input': instance['question'], 'context_table': instance['context']}
        )
        error = ''
    except Exception as e:
        result = {'query': ''}
        error = str(e).split('\n')[0]  # Get only the first line of the error message

    results.append(
        dict(
            question=instance['question'],
            answer=instance['query'].strip(),
            context=instance['context'],
            result=result['query'].strip(),
            model_name=model_name,
            temperature=temperature,
            error=error
        )
    )
    result_queries.append(result['query'].strip())
    gold_queries.append(f"{instance['query'].strip()}\t{instance['db_id']}")

# Export results and run evaluation
store_results(
    _results=results,
    _result_queries=result_queries,
    _gold_queries=gold_queries,
    _model_name=model_name,
    _temperature=temperature,
    _reference=reference
)
