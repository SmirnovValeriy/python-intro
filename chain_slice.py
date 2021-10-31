from itertools import chain


def chainslice(begin, end, *args):
    for i, num in enumerate(chain(*args)):
        if i >= begin:
            if i < end:
                yield num
            else:
                break
