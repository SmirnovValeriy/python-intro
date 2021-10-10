def det_matrix(matrix):
    answer = 0
    n = len(matrix[0])
    if n == 1:
        return matrix[0][0]
    else:
        for i, m in enumerate(matrix[0]):
            answer += (-1) ** i * m * det_matrix(
                [
                    [
                        elem
                        for j, elem in enumerate(matrix[k])
                        if j != i
                    ]
                    for k in range(1, n)
                ]
            )
    return answer


matrix = eval(input())
print(det_matrix(matrix))
