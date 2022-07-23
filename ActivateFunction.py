from math import exp
import numpy as np

def ReLU(n):
    '''
    Activation function ReLU
    :param n:
    :return: a
    '''
    #scale = lambda x 
    return max(0, n)


def Purelin(n):
    return n


def Hardlim(n):
    return np.where(n<0, 0 , 1)


def Hardlims(n):
    return np.where(n<0, -1 , 1)


def Satlin(n):
    scale = lambda x: clamp(x, 0, 1)
    return scale(n)


def clamp(n, min, max):
    if min > max:
        min, max = max, min
    if n < min:
        return min
    elif n > max:
        return max
    return n


def Satlins(n):
    scale = lambda x: clamp(x, -1, 1)
    return scale(n)


def Logsid(n):
    return Logsid_scale(n)
Logsid_scale = lambda x: 1 / (1 + np.exp(-x))

def Tansig(n):
    return Tansig_scale(n)
Tansig_scale = lambda x: (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))