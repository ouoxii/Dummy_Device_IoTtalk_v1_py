import csv, os
import numpy as np
import pandas as pd
import json

# 'line.csv' 這個手勢怪怪的

files = [ 'circle2.csv', 'lift.csv','other.csv']

x = []
y = []
data_size = 8
for label, f in enumerate(files):
    with open(os.path.join('csv_data', f)) as file:
        data=csv.reader(file)
        queue = list()
        t = 0
        for row in data:
            row = [float(k) for k in row]
            queue.append(row)
            if len(queue) > data_size:
                t += 1
                queue.pop(0)
            if len(queue) == data_size:
                temp = np.array(queue).T.flatten().tolist()
                x.append(temp)
                y.append(label)
            if t == 2:
                queue = list()
                t = 0

with open('data.json', 'w') as file:
    json.dump({'x':x, 'y':y}, file, indent=4)

