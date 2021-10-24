from math import sqrt


def dist(coord_0, coord_1):
    return sqrt(sum([(c_0 - c_1) ** 2 for c_0, c_1 in zip(coord_0, coord_1)]))


galaxies = []
while ' ' in (inp_ := input()):
    x, y, z, name = inp_.split()
    galaxies.append(((float(x), float(y), float(z)), name))

max_dist = 0
max_pair = None
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        if (dist_ := dist(galaxies[i][0], galaxies[j][0])) > max_dist:
            max_dist = dist_
            max_pair = (galaxies[i][1], galaxies[j][1])

print(' '.join(sorted(max_pair)))
