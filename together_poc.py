from pydantic_models import SQLQuery, Tables
from eval import execute_query_same_str
from langchain_together import ChatTogether  # noqa
from langchain_openai.chat_models import ChatOpenAI  # noqa
from utils import load_sql_dataset  # noqa
from gen_ai import generate
from templates import DummyTable, SQLPrompt

model = ChatTogether(
    # together_api_key="YOUR_API_KEY",
    # model="meta-llama/Llama-2-70b-chat-hf",
    model="meta-llama/Llama-3-70b-chat-hf",
    # model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    temperature=0.0
)
# model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)

print('Downloading the data')
# data = load_sql_dataset()
# instance = data['train'][0]  # TODO this needs as loop
instance = {
    'context': 'CREATE TABLE management (department_id VARCHAR); CREATE TABLE department (department_id VARCHAR)',
    'question': 'How many departments are led by heads who are not mentioned?',
    'answer': 'SELECT COUNT(*) FROM department WHERE NOT department_id IN (SELECT department_id FROM management)'
}

dummy_table = generate(
    prompt=DummyTable(pydantic_model=Tables),
    model=model,
    _input={'user_context': instance['context'], 'user_question': instance['question']}
)
tables_dict = dummy_table.create_tables()

result = generate(
    prompt=SQLPrompt(pydantic_model=SQLQuery),
    model=model,
    _input={'user_input': instance['question'], 'context_table': instance['context']}
)
print(result)

print(execute_query_same_str(instance['answer'], result.query, tables_dict))
