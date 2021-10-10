n_tmp = n = int(input())
n_r = 0
while n_tmp % 10:
    n_r = n_r * 10 + n_tmp % 10
    n_tmp = n_tmp // 10
print('YES' if n == n_r else 'NO')
