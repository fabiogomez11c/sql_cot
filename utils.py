from typing import List, Dict
from datasets.arrow_dataset import Dataset
from dspy import Example
from datasets import load_dataset
import pandas as pd
import json
import os
import re
import sqlite3


def examples_from_dataset(dataset: Dataset) -> List[Example]:
    """Convert the dataset to a list of examples"""
    return [
        Example(
            question=row['question'],
            answer=row['answer'],
            context=row['context']
        ).with_inputs('question', 'context') for row in dataset
    ]


def load_sql_dataset() -> Dataset:
    """Load the dataset from the b-mc2/sql-create-context dataset"""
    dataset = Dataset.from_dict(load_dataset("b-mc2/sql-create-context"))
    dataset = dataset.select(range(500))
    # dataset = dataset.shuffle()
    # dataset = dataset.train_test_split(test_size=0.2)
    # dataset = dataset.map(lambda x: x['train'])
    # dataset = dataset.remove_columns(['train'])
    return dataset


def load_dict_dataset() -> dict:
    """Load the dataset from the data.json file and return it as a dictionary"""
    with open("data.json", "r") as file:
        data = json.load(file)
    return data


def get_database_folders() -> List[str]:
    """Retrieve all folder names inside the 'database' directory."""
    database_path = os.path.join(os.getcwd(), 'database')
    folders = [name for name in os.listdir(database_path) if os.path.isdir(os.path.join(database_path, name))]
    return folders


def get_sql_files_in_folder(folder_path: str) -> List[str]:
    """Retrieve all .sql files inside the specified folder."""
    files = [file for file in os.listdir(folder_path) if file.endswith('.sql')]
    return files


def get_sqlite_files_in_folder(folder_path: str) -> List[str]:
    """Retrieve all .sqlite files inside the specified folder."""
    files = [file for file in os.listdir(folder_path) if file.endswith('.sqlite')]
    return files


def extract_create_table_commands(folders: List[str]) -> dict:
    """Extracts CREATE TABLE commands from .sql files in given folders."""
    all_commands = {}
    for folder in folders:
        folder_path = os.path.join('database', folder)
        sqlite_files = get_sql_files_in_folder(folder_path)
        for sqlite_file in sqlite_files:
            file_path = os.path.join('database', folder, sqlite_file)
            with open(file_path) as file:
                content = file.read()
                # Extract CREATE TABLE commands and clean newlines
                commands = re.findall(r'CREATE TABLE.*?;', content.replace('\n', ' ').replace('\t', ' '), re.DOTALL)
                table_names = [re.search(r'CREATE TABLE(?: IF NOT EXISTS)?\s+["`\[]?(\w+)["`\]]?', command).group(1)
                               for command in commands if re.search(r'CREATE TABLE(?: IF NOT EXISTS)?\s+["`\[]?(\w+)["`\]]?', command)]
                for table_name, command in zip(table_names, commands):
                    all_commands[table_name] = command
    return all_commands


def extract_database_schema(folders: List[str]) -> dict:
    """Extracts the schema from all SQLite databases in the given folders."""
    result = {}
    for folder in folders:
        folder_path = os.path.join('database', folder)
        sqlite_files = get_sqlite_files_in_folder(folder_path)
        sqlite_files = [os.path.join('database', folder, sqlite_file) for sqlite_file in sqlite_files]

        for db in sqlite_files:
            schema = {}
            conn = sqlite3.connect(db)
            cursor = conn.cursor()

            # fetch table names
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [str(table[0].lower()) for table in cursor.fetchall()]

            # fetch table info
            for table in tables:
                cursor.execute("SELECT sql FROM sqlite_master")
                schema[table] = ' '.join(cursor.fetchone()[0].replace('\n', '').replace('\t', '').split())

            result.update(schema)

    return result


def get_table_data(table: str, db: str) -> str:
    """Get the data from the specified table and return it as a string with a nice formatting specifying
    the column and the rows of the table."""
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    # Safely parameterize table name to avoid SQL injection
    cursor.execute("PRAGMA table_info(" + table + ")")
    columns = [description[1] for description in cursor.fetchall()]
    # Safely parameterize table name to avoid SQL injection
    cursor.execute("SELECT * FROM " + table)
    rows = cursor.fetchall()
    formatted_data = f"Table: {table}\nColumns: {', '.join(columns)}\nRows:\n"
    for row in rows:
        formatted_data += ' | '.join(str(item) for item in row) + '\n'
    return formatted_data + "\n"


def load_prepare_dev_dataset() -> List[Dict]:
    """Load the dev.json dataset and prepare the data according to each question"""
    # load json
    with open('dev.json', 'r') as file:
        data = json.load(file)

    # iterate over each question and get the create context of the table
    for question in data:
        # get the sqlite files
        question_table = question['db_id']
        folder_path = os.path.join('database', question_table)
        sqlite_files = get_sqlite_files_in_folder(folder_path)
        sqlite_files = [os.path.join('database', question_table, sqlite_file) for sqlite_file in sqlite_files]

        # extract schema
        schema = extract_database_schema([question_table])
        tables = ""
        for table in schema.keys():
            tables += get_table_data(table, sqlite_files[0])
        question['context'] = tables

    return data


def store_results(_results: List[Dict], _result_queries: List[str], _gold_queries: List[str], _model_name: str, _temperature: str, _reference: str) -> None:
    """Store the results in several files"""

    # Export results and run evaluation
    df = pd.DataFrame(_results)
    df.to_csv(f'./results/results_{_model_name.replace("/", "_")}_{_temperature}_{_reference}.csv', index=False)

    results_path = f"./results/results_{_model_name.replace('/', '_')}_{_temperature}_{_reference}.sql"
    with open(results_path, "w") as f:
        for result in _result_queries:
            f.write(result + "\n")

    gold_path = f"./results/gold_{_model_name.replace('/', '_')}_{_temperature}_{_reference}.sql"
    with open(gold_path, "w") as f:
        for result in _gold_queries:
            f.write(result + "\n")
