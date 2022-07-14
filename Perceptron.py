import ActivateFunction as af
class Perceptron:
    _W = None
    _b = None
    _i = 1
    def __init__(self, W = None, b = None, i = None):
        self._b = b
        self._W = W
        self._i = i
    def fit(self, X, y):
        print(X.shape(0))

#        for label in y:
#            a = af.Hardlims(self._W.T @ self._p)
#            e = y[0] - a
#            self._W = self._W + e @ self._p.T
#            self._b = self._b + e