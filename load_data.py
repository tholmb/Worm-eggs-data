import numpy as np
import pickle

with open('wormeggs.pkl', 'rb') as f:
    loaded = pickle.load(f)
data, labels = loaded[0], loaded[1]
print(data.shape)
print(labels.shape)