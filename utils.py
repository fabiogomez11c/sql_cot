from typing import List
from datasets.arrow_dataset import Dataset
from dspy import Example
from datasets.arrow_dataset import Dataset
from datasets import load_dataset


def examples_from_dataset(dataset: Dataset) -> List[Example]:
    """Convert the dataset to a list of examples"""
    return [
        Example(
            question=row['question'],
            answer=row['answer'],
            context=row['context']
        ).with_inputs('question', 'context') for row in dataset
    ]


def load_dataset() -> Dataset:
    """Load the dataset from the b-mc2/sql-create-context dataset"""
    dataset = Dataset.from_dict(load_dataset("b-mc2/sql-create-context"))
    dataset = dataset.select(range(80))
    dataset = dataset.shuffle()
    dataset = dataset.train_test_split(test_size=0.2)
    dataset = dataset.map(lambda x: x['train'])
    dataset = dataset.remove_columns(['train'])
    return dataset
