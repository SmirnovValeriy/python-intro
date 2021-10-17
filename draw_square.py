def squares(w, h, *args):
    image = [['.'] * w for _ in range(h)]
    for X, Y, s, c in args:
        for i in range(Y, Y + s, 1):
            image[i][X:X+s] = c * s
    print('\n'.join([''.join(row) for row in image]))
