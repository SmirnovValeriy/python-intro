from random import randint
from itertools import cycle


def randomes(args):
    args = [tuple(arg) for arg in args]
    for tup in cycle(args):
        yield randint(*tup)
