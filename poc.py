from datasets.arrow_dataset import Dataset
from datasets import load_dataset

import dspy
from dspy.teleprompt import BootstrapFewShotWithRandomSearch, MIPRO
from dspy.evaluate import Evaluate

from utils import examples_from_dataset
from metric import exact_match

import logging

# Configure logging to store logs in a file without printing them to the console
logging.basicConfig(
    filename='app.log',
    filemode='w', format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Dataset handling/importing
dataset = Dataset.from_dict(load_dataset("b-mc2/sql-create-context"))
dataset = dataset.select(range(80))
dataset = dataset.shuffle()
dataset = dataset.train_test_split(test_size=0.2)
dataset = dataset.map(lambda x: x['train'])
dataset = dataset.remove_columns(['train'])

# Create the example dataset for dspy
train_examples = examples_from_dataset(dataset['train'])
test_examples = examples_from_dataset(dataset['test'])

# model = dspy.OllamaLocal(model='llama3')
model = dspy.OllamaLocal(model='phi3')
# model = dspy.OpenAI(model='gpt-3.5-turbo-0125', max_tokens=1000)
dspy.settings.configure(lm=model)

basic_prompt = dspy.ChainOfThought("question -> answer")


class CoTwithContext(dspy.Module):
    def __init__(self):
        super().__init__()
        self.program = dspy.ChainOfThought("context, question -> answer")

    def forward(self, context, question):
        return self.program(context=context, question=question)


cot_with_context = CoTwithContext()

evaluate = Evaluate(
    devset=test_examples,
    metric=exact_match,
    display_progress=True,
    num_threads=4
)

# evalute without optim
print("EVAL W/O OPTIMIZATION +++++++++++++++++++++")
print("Basic prompt")
evaluate(basic_prompt)
print("COT with context")
evaluate(cot_with_context)

# optimization
config_bootstrap = dict(
    max_bootstrapped_demos=8,
    max_labeled_demos=8,
    num_candidate_programs=10
)
config_mipro = dict(
    num_candidates=5,
    init_temperature=1.0,
)
teleprompter = MIPRO(
    metric=exact_match,
    **config_mipro
)
print("OPTIMIZATION +++++++++++++++++++++")
print("COT with context")
opt_cot_with_context = teleprompter.compile(
    cot_with_context,
    trainset=train_examples,
    num_trials=5,
    max_bootstrapped_demos=8,
    max_labeled_demos=8,
    eval_kwargs={'num_threads': 4}
)

# evalute after optim
print("EVAL AFTER OPTIMIZATION +++++++++++++++++++++")
print("COT with context")
evaluate(opt_cot_with_context)
