from itertools import groupby


def LookSay():
    lst = [1]
    while True:
        for num in lst:
            yield num
        iter_ = groupby(lst)
        lst = []
        for key, group in iter_:
            lst.append(len(list(group)))
            lst.append(key)
