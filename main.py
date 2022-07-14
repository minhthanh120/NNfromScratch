import numpy as np
from Perceptron import Perceptron
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("iris.data", delimiter=",")

    print(data.sample(frac=1, random_state=12).reset_index(drop=True).head(5))
    b = np.array([3, 3]).T
    W = np.array([[1, -1, -1], [1, 1, -1]])
    p = np.array([-1, -1, -1]).T
    n = W @ p + b
    model = Perceptron(W, 1, 1)
    model.fit(W, p)
