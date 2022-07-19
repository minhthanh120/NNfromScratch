import numpy as np

from ActivateFunction import Hardlim


class Perceptron:
    _W = None
    _b = None
    _a = None
    _i = 1

    def __init__(self, W=None, b=None, i=None):
        self._W = W
        self._b = 0
        self._i = i

    def fit(self, X, y):
        d = X.shape[1]
        if self._W is None:
            self._W = np.zeros(d).reshape(1, -1)
        for p, label in zip(X, y):
            n = self._W @ p.reshape(-1, 1) + self._b
            self._a = Hardlim(n)
            self.PLA_rule(p, label)

    def PLA_rule(self, p, label):
        e = label - self._a
        self._W = self._W + e*p
        self._b = self._b + e

    def predict(self, X):
        n = self._W @ X.reshape(-1, 1)+self._b
        return Hardlim(n)

    def score(self, X, y):
        for x, label in zip(X, y):
            self.predict(x)
