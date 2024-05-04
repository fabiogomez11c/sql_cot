from typing import List
from datasets.arrow_dataset import Dataset
from dspy import Example


def examples_from_dataset(dataset: Dataset) -> List[Example]:
    return [
        Example(
            question=row['question'],
            answer=row['answer'],
            context=row['context']
            ).with_inputs('question', 'context') for row in dataset
        ]
