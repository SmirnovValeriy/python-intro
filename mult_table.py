from math import ceil
"""
max length of f'{n} * {m} = {k}'
equals 4 (spaces) + 2 ('*' and '=') + 2 * len(N) + len(N * N)
"""
N, M = eval(input())
max_len = 4 + 2 + 2 * len(str(N)) + len(str(N * N))
str_len = max_len
num_ = 1
table = []
prods = [
            [
                (
                    f"{i}".rjust(len(str(N))) +
                    " * " + f"{j}".ljust(len(str(N))) +
                    f" = {i*j}"
                ).ljust(max_len)
                for i in range(1, N+1)
            ] for j in range(1, N+1)
        ]
while str_len + 3 + max_len <= M:
    str_len += 3 + max_len
    num_ += 1
for i in range(ceil(N / num_)):
    table.append('=' * M)
    for j in range(N):
        table.append(' | '.join(prods[j][i*num_:(i+1)*num_]))
table.append('=' * M)
print('\n'.join(table))
