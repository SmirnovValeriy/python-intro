M, N = eval(input())

matrix = [[0] * M for _ in range(N)]

i, j = 0, 0
step = 1
counter = 0
N_cnt = N - 1
M_cnt = M

while counter < N*M:
    for _ in range(M_cnt):
        matrix[i][j] = counter % 10
        j += step
        counter += 1
    j -= step
    i += step
    for _ in range(N_cnt):
        matrix[i][j] = counter % 10
        i += step
        counter += 1
    i -= step
    step = -step
    j += step
    N_cnt -= 1
    M_cnt -= 1

for i in range(N):
    print(*matrix[i], sep=' ')
