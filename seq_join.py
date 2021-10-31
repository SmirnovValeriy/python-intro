def joinseq(*args):
    args = [iter(arg) for arg in args]
    cur = {key: next(iter_, None) for key, iter_ in enumerate(args)}
    cur = {key: value for key, value in cur.items() if value}
    while cur.keys():
        key_min = min(cur.keys(), key=cur.__getitem__)
        yield cur[key_min]
        if next_ := next(args[key_min], None):
            cur[key_min] = next_
        else:
            del cur[key_min]
