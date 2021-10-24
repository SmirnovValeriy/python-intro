from random import choice


N = int(input())

with open('anna_.txt', 'r') as f:
    text = f.read().replace('\n    ', ' @ ').split()

dict_ = {}
for w in zip(text[:-2], text[1:-1], text[2:]):
    dict_[w[:2]] = dict_.get(w[:2], [])
    dict_[w[:2]].append(w[2])

if N == 1:
    print(choice(text).replace('@', '\n    '))
elif N == 2:
    print(' '.join(choice(list(dict_.keys()))).replace(' @ ', '\n    '))
else: # N >= 3
    answer = list(choice(list(dict_.keys())))
    i = 0
    while i < N - 2:
        answer.append(choice(dict_[tuple(answer[i:i+2])]))
        i += 1
    print(' '.join(answer).replace(' @ ', '\n    '))
