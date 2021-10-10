def divdigit(N: int) -> int:
    N_copy = N
    answer = 0
    while N_copy:
        digit = N_copy % 10
        if digit == 0:
            pass
        else:
            answer += N % digit == 0
        N_copy = N_copy // 10
    return answer
