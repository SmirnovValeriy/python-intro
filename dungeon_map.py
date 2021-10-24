dirs = {}

while ' ' in (inp := input()):
    a, b = inp.split(' ')
    dirs[a] = dirs.get(a, set())
    dirs[a].add(b)
    dirs[b] = dirs.get(b, set())
    dirs[b].add(a)

in_ = inp
out_ = input()

seen = set()
cur = [in_]
while True:
    if len(cur) == 0:
        print('NO')
        break
    if out_ in cur:
        print('YES')
        break
    seen = seen.union(cur)
    cur = [dir_ for key in cur for dir_ in dirs[key] if dir_ not in seen]
