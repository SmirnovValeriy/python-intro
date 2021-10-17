from decimal import *


def pi():
    getcontext().prec = 1010
    pi_ = Decimal(3)
    pi_pred = 0
    mul = pi_
    n, n_add = 1, 0
    d, d_add = 0, 24
    while pi_ != pi_pred:
        pi_pred = pi_
        n, n_add = n + n_add, n_add + 8
        d, d_add = d + d_add, d_add + 32
        mul = (mul * n) / d
        pi_ += mul
    return +pi_


def sin(x):
    getcontext().prec = 1010
    sin_ = x
    sin_pred = 0
    i = 1
    sgn = 1
    n = x
    d = 1
    while sin_ != sin_pred:
        sin_pred = sin_
        i += 2
        n *= x * x
        d *= i * (i-1)
        sgn *= -1
        sin_ += sgn * n / d
    return +sin_


def cos(x):
    getcontext().prec = 1010
    cos_ = 1
    cos_pred = 0
    i = 0
    sgn = 1
    n = 1
    d = 1
    while cos_ != cos_pred:
        cos_pred = cos_
        i += 2
        n *= x * x
        d *= i * (i-1)
        sgn *= -1
        cos_ += sgn * n / d
    return +cos_


A = eval(input())
E = eval(input())

A_rad = A * pi() / 200
sin_ = sin(A_rad)
cos_ = cos(A_rad)
getcontext().prec = E
print(sin_ / cos_)
