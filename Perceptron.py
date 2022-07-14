import numpy as np

from ActivateFunction import Hardlim
class Perceptron:
    _W = None
    _b = None
    _a = None
    _i = 1
    def __init__(self, W = None, b = None, i = None):
        self._W = W
        self._b = 0
        self._i = i
    def fit(self, X, y):
        d = X.shape[1]
        if W is None:
            self._W = np.zeros(d).reshape
        for x in X:
            n = self._W.T@x
            self._a = Hardlim(n)
            