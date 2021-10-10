from functools import reduce


def BinPow(a: object, n: int, f):
    if n == 1:
        return a
    elif n % 2:
        return f(BinPow(a, n-1, f), a)
    else:
        return f(BinPow(a, n//2, f), BinPow(a, n//2, f))
