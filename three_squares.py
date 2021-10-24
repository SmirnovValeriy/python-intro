from math import sqrt


inp_set = set(eval(input()))
max_elem = max(inp_set)
three_squares = set(
    m * m + n * n + k * k
    for m in range(1, int(max_elem ** 0.5) + 1)
    for n in range(m, int((max_elem - m * m) ** 0.5) + 1)
    for k in range(n, int((max_elem - m * m - n * n) ** 0.5) + 1)
)

print(len(inp_set.intersection(three_squares)))
