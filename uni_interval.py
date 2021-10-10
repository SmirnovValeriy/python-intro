intervals = sorted(eval(input()))

start, end = None, None
merged_intervals = []
for interval in intervals:
    if end is None:
        start = interval[0]
        end = interval[1]
    elif end < interval[0]:
        merged_intervals.append([start, end])
        start = interval[0]
        end = interval[1]
    else:
        end = max([end, interval[1]])
if start is not None:
    merged_intervals.append([start, end])

answer = 0
for interval in merged_intervals:
    answer += interval[1] - interval[0]
print(answer)
