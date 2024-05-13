"""Script to generate dummy tables for later evaluation of the model"""
from utils import load_sql_dataset
from gen_ai import generate
from templates import DummyTable
from pydantic_models import Tables
from langchain_openai.chat_models import ChatOpenAI
from sqlglot.executor import execute
from tqdm import tqdm
import json

model = ChatOpenAI(temperature=0.0)
data = load_sql_dataset()

results = []
progress_bar = tqdm(data['train'], total=len(data['train']))
for instance in progress_bar:

    try:
        # generate a dummy table
        dummy_table = generate(
            prompt=DummyTable(pydantic_model=Tables),
            model=model,
            _input={'user_context': instance['context'], 'user_question': instance['question']}
        )

        # generate the tables
        table_pydantic = Tables.from_dict(dummy_table['tables'])
        tables_dict = table_pydantic.create_tables()
    except Exception as e:
        print(e)
        continue

    # check if the correct answer is executable
    try:
        execute(instance['answer'], tables=tables_dict)
    except Exception:
        continue

    # store tables
    instance['dummy_table'] = tables_dict
    results.append(instance)
    progress_bar.set_description(f"Processed: {len(results)}")

    with open('data.json', 'w') as f:
        json.dump(results, f)
