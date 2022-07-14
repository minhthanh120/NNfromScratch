from math import exp


def ReLU(n):
    '''
    Activation function ReLU
    :param n:
    :return: a
    '''
    return max(0, n)


def Purelin(n):
    return n


def Hardlim(n):
    if n < 0: return 0
    return 1


def Hardlims(n):
    if n < 0: return -1
    return 1


def Satlin(n):
    return clamp(n, 0, 1)


def clamp(n, min, max):
    if min > max:
        min, max = max, min
    if n < min:
        return min
    elif n > max:
        return max
    return n


def Satlins(n):
    return clamp(n, -1, 1)


def Logsid(n):
    return 1 / (1 + exp(-n))


def Tansig(n):
    return (exp(n) - exp(-n)) / (exp(n) + exp(-n))
