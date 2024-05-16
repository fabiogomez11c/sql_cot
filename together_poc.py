from pydantic_models import SQLQuery
from eval import execute_query_same_str, evaluate_with_llm
from langchain_together import ChatTogether  # noqa
from langchain_openai.chat_models import ChatOpenAI  # noqa
from utils import load_prepare_dev_dataset  # noqa
from gen_ai import generate
from templates import SQLPrompt
from tqdm import tqdm
import pandas as pd

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

# Export results
df = pd.DataFrame(results)
df.to_csv(f'./results/results_{model_name.replace("/", "_")}_{temperature}.csv', index=False)

with open(f"./results/results_{model_name.replace('/', '_')}_{temperature}.sql", "w") as f:
    for result in result_queries:
        f.write(result + "\n")

with open(f"./results/gold_{model_name.replace('/', '_')}_{temperature}.sql", "w") as f:
    for result in gold_queries:
        f.write(result + "\n")
