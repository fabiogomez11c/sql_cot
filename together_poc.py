from pydantic_models import SQLQuery
from eval import execute_query_same_str
from langchain_together import ChatTogether  # noqa
from langchain_openai.chat_models import ChatOpenAI  # noqa
from utils import load_dict_dataset  # noqa
from gen_ai import generate
from templates import SQLPrompt
from tqdm import tqdm
import pandas as pd

temperature = 0.0
# model_name = "meta-llama/Llama-3-70b-chat-hf"
# model_name = "gpt-3.5-turbo-0125"
# model_name = "meta-llama/Llama-2-70b-chat-hf"
model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"
model = ChatTogether(
    model=model_name,
    temperature=temperature
)
# model = ChatOpenAI(model=model_name, temperature=0.0)

print('Downloading the data')
data = load_dict_dataset()

results = []
correct_count = 0
correct_error = 0
progress_bar = tqdm(data, total=len(data))
for instance in progress_bar:
    tables_dict = instance['dummy_table']

    try:
        result = generate(
            prompt=SQLPrompt(pydantic_model=SQLQuery),
            model=model,
            _input={'user_input': instance['question'], 'context_table': instance['context']}
        )
        is_correct = execute_query_same_str(instance['answer'], result['query'], tables_dict)
    except Exception as e:
        result = {'query': ''}
        error = str(e).split('\n')[0]  # Get only the first line of the error message
        is_correct = (False, instance['answer'], '', error)

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
df.to_csv(f'./results/results_{model_name.replace("/", "_")}_{temperature}.csv', index=False)
