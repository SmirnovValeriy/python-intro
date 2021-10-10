from math import log
'''
n = k^p
log_k(n) = p * log_k(k)
p = log_k(n)
"YES" if p is integer
"NO" else
'''
prec = 1e-10
n = int(input())
answer = 'NO'
for k in range(2, n):
    if abs(int(log_ := log(n, k)) - log_) < prec:
        answer = 'YES'
        break

print(answer)
