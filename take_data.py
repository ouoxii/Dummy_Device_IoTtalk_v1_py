import json
import numpy as np
import random
from sklearn.model_selection import train_test_split, StratifiedKFold
def get_x_y():
    file = 'data.json'
    with open(file, 'r') as f:
        data = json.load(f)
        x = data['x']
        y = data['y']
    return x, y


def train_test_split_data(test_size = 0.1):
    x, y = get_x_y()
    train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=test_size, stratify=y, random_state=87)
    
    return train_x, train_y, test_x, test_y


def k_fold(n_splits=10):
    x, y = get_x_y()
    x = np.array(x)
    y = np.array(y)
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=87)
    for train_ind, test_ind in skf.split(x, y):
        yield x[train_ind].tolist(), y[train_ind].tolist(), x[test_ind].tolist(), y[test_ind].tolist()

