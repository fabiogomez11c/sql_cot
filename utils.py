from typing import List
from datasets.arrow_dataset import Dataset
from dspy import Example
from datasets import load_dataset
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
    """Retrieve all .sqlite files inside the specified folder."""
    files = [file for file in os.listdir(folder_path) if file.endswith('.sql')]
    return files


def get_sqlite_files_in_folder(folder_path: str) -> List[str]:
    """Retrieve all .sqlite files inside the specified folder."""
    files = [file for file in os.listdir(folder_path) if file.endswith('.sqlite')]
    return files


def extract_create_table_commands(folders: List[str]) -> dict:
    """Extracts CREATE TABLE commands from .sqlite files in given folders."""
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
