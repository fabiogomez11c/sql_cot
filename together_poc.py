from typing import List, Dict, Any
from sqlglot.executor import execute
from sqlglot import diff, parse_one
from pydantic import BaseModel, Field
from langchain_together import ChatTogether
from langchain_openai.chat_models import ChatOpenAI  # noqa
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from utils import load_sql_dataset

# model = ChatTogether(
#     # together_api_key="YOUR_API_KEY",
#     # model="meta-llama/Llama-2-70b-chat-hf",
#     model="meta-llama/Llama-3-70b-chat-hf",
#     # model="mistralai/Mixtral-8x7B-Instruct-v0.1",
#     temperature=0.0
# )
model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.0)


class SQLQuery(BaseModel):
    """Generated SQL query"""
    query: str = Field(..., description='Generated SQL query')


class DataRow(BaseModel):
    """Data inside a table"""
    data: Dict[str, Any] = Field(..., description='One row of data, first element is the id')

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a data row from a dictionary"""
        return cls(data=data['data'])

    def create_row(self) -> Dict[str, Any]:
        """Create a row"""
        return self.data


class Table(BaseModel):
    """Table with a list of data"""
    tableName: str = Field(..., description='Name of the table')
    tableData: List[DataRow] = Field(..., description='All the rows of the table')

    def create_table(self) -> List:
        """Create a table"""
        return [row.create_row() for row in self.tableData]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create a table from a dictionary"""
        return cls(tableName=data['tableName'], tableData=[DataRow.from_dict(row) for row in data['tableData']])


class Tables(BaseModel):
    """All the tables in the database"""
    tables: Dict[str, Table] = Field(..., description='All the tables in the database')

    def create_tables(self) -> Dict[str, List]:
        """Create all the tables"""
        return {table_name: table.create_table() for table_name, table in self.tables.items()}

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Create tables from a dictionary"""
        return cls(tables={table_name: Table.from_dict(table) for table_name, table in data.items()})


print('Downloading the data')
data = load_sql_dataset()
instance = data['train'][0]

print("Generating the dummy table")
parser = JsonOutputParser(pydantic_object=Tables)
prompt_template = PromptTemplate(
    template="Generate a dummy table with 5 rows that corresponds to:\n{user_context}\nThat could answer a question like:\n{user_question}\nWith the following format:\n{format_instructions}",  # noqa
    input_variables=['user_context', 'user_question'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)
chain = prompt_template | model | parser
dummy_table = chain.invoke({'user_context': instance['context'], 'user_question': instance['question']})
print(dummy_table)

tables = Tables.from_dict(dummy_table['tables'])
tables_dict = tables.create_tables()

print('Setting up the prompt')
parser = JsonOutputParser(pydantic_object=SQLQuery)
prompt_template = PromptTemplate(
    template="Answer the question with the format:\n{format_instructions}\nGive me a query that could answer the question: {user_input}?\nContext table: {context_table}",  # noqa
    input_variables=['user_input'],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

print("Setting up the chain")
chain = prompt_template | model | parser
print("Invoking the chain")
result = chain.invoke({'user_input': instance['question'], 'context_table': instance['context']})
print(result)


# execute("select * from head", tables=tables_dict)
correct = execute(instance['answer'], tables=tables_dict)
prediction = execute(result['query'], tables=tables_dict)
