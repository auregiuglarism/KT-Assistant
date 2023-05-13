import sklearn as sk
import numpy as np
import pandas as pd
import json
from torch.utils.data import Dataset, DataLoader

class BQDataset():
    def __init__(self, path):
        self.dataset = open(path,encoding="utf-8")

        self.dataset = [json.loads(instance) for instance in self.dataset ]

    def get_dataset(self):
        return self.dataset
#
# train_dataset = BoolQDataset('datasets/train.jsonl')
# val_dataset = BoolQDataset('datasets/dev.jsonl')
#test_dataset = BoolQDataset('test.json')


bqd = BQDataset("datasets/train.jsonl")
a = bqd.get_dataset()[1]

print(a["question"])
