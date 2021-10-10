pred = input()
counter = 0
while True:
    cur = input()
    if cur[0] == '-':
        break
    i = 0
    pred_sym = '.'
    while i < len(cur):
        if cur[i] == '#':
            if pred[i] != '#' and pred_sym == '.':
                counter += 1
        pred_sym = cur[i]
        i += 1
    pred = cur
print(counter)
