from itertools import (
    count,
    cycle,
    repeat,
    chain,
    islice,
    combinations,
    permutations,
    product
)

experiment_ids = count(100)

for experiment_id in islice(experiment_ids, 5):
    print(experiment_id)

data_centers = ["Chennai", "Mumbai", "Bangalore"]

for center in islice(cycle(data_centers), 7):
    print(center)

for config in repeat("production", 3):
    print(config)

dataset_1 = ["train_1", "train_2"]
dataset_2 = ["validation_1", "validation_2"]
dataset_3 = ["test_1"]

for data in chain(dataset_1, dataset_2, dataset_3):
    print(data)

numbers = count(1)

for number in islice(numbers, 5):
    print(number)

features = ["Age", "Salary", "Experience"]

for pair in combinations(features, 2):
    print(pair)

for arrangement in permutations(features, 2):
    print(arrangement)

models = ["RandomForest", "XGBoost"]
depths = [5, 10]
learning_rates = [0.01, 0.1]

for model, depth, learning_rate in product(
    models,
    depths,
    learning_rates
):
    print(model, depth, learning_rate)