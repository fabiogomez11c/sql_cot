from pydantic_models import SQLQuery, Tables
from eval import execute_query_same_str
from langchain_together import ChatTogether  # noqa
from langchain_openai.chat_models import ChatOpenAI  # noqa
from utils import load_dict_dataset  # noqa
from gen_ai import generate
from templates import SQLPrompt
from tqdm import tqdm
import pandas as pd

model_name = "meta-llama/Llama-3-70b-chat-hf"
temperature = 0.0
# model_name = "meta-llama/Llama-2-70b-chat-hf"
# model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
model = ChatTogether(
    # together_api_key="YOUR_API_KEY",
    # model="meta-llama/Llama-2-70b-chat-hf",
    model=model_name,
    # model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=temperature
)
# model = ChatOpenAI(temperature=0.0)

print('Downloading the data')
data = load_dict_dataset()

results = []
correct_count = 0
correct_error = 0
progress_bar = tqdm(data, total=len(data))
for instance in progress_bar:
    dummy_table = instance['dummy_table']
    tables = Tables.from_dict(dummy_table)
    tables_dict = tables.create_tables()

    result = generate(
        prompt=SQLPrompt(pydantic_model=SQLQuery),
        model=model,
        _input={'user_input': instance['question'], 'context_table': instance['context']}
    )

    is_correct = execute_query_same_str(instance['answer'], result['query'], tables_dict)
    results.append(
        dict(
            question=instance['question'],
            answer=instance['answer'],
            context=instance['context'],
            result=result['query'],
            is_correct=is_correct[0],
            model_name=model_name,
            correct=is_correct[1],
            prediction=is_correct[2],
            error=is_correct[3],
            temperature=temperature
        )
    )
    if is_correct[0]:
        correct_count += 1
    if is_correct[1] == '':
        correct_error += 1
    progress_bar.set_description(
        f"Accuracy: {correct_count / (len(results) - correct_error):.2%} ({correct_count}/{len(results) - correct_error})")  # noqa

# Export results
df = pd.DataFrame(results)
df.to_csv(f'results/results_{model_name}_{temperature}.csv', index=False)
