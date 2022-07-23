import numpy as np

from ActivateFunction import Hardlim


class Perceptron:
    _W = None
    _b = None
    _a = None
    _i = 1
    _eta = None

    def __init__(self, W=None, b=None, i=1, eta = 0.01):
        self._W = W
        self._b = 0
        self._i = i
        self._eta = eta

    def fit(self, X, y):
        d = X.shape[1]
        if self._W is None:
            self._W = np.zeros(d).reshape(1, -1)
        for _ in range(self._i):
            for p, label in zip(X, y):
                n = self._W @ p.reshape(-1, 1) + self._b
                self._a = Hardlim(n)
                self.PLA_rule(p, label)

    def PLA_rule(self, p, label):
        e = label - self._a
        self._W = self._W + e*p
        self._b = self._b + es

    def predict(self, X):
        if X.shape[-1] >1:
            for x in X:
                n = self._W @ x.reshape(-1, 1)+self._b
        n = self._W @ X.reshape(-1, 1)+self._b
        return Hardlim(n)
