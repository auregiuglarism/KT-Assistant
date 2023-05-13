import sklearn as sk
import numpy as np
import pandas as pd
import json
from torch.utils.data import Dataset, DataLoader
np.
np.
class BoolQDataset(Dataset):
    def __init__(self, path):
        with open(path) as f:
            data = json.load(f)
        self.questions = [d['question'] for d in data]
        self.passages = [d['passage'] for d in data]
        self.answers = [int(d['answer']) for d in data]

    def __len__(self):
        return len(self.questions)

    def __getitem__(self, idx):
        return self.questions[idx], self.passages[idx], self.answers[idx]

train_dataset = BoolQDataset('train.json')
val_dataset = BoolQDataset('val.json')
test_dataset = BoolQDataset('test.json')

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=32)
test_loader = DataLoader(test_dataset, batch_size=32)

print(dataset)

np.