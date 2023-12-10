import numpy as np

values = [[int(v) for v in line.strip().split()] for line in open("input/d9")]

total = [0, 0]
for v in values:
    t = v
    last_v = [v[-1]]
    while not np.all((t := np.diff(t))[:] == 0):
        last_v.append(t[-1])

    total[1] += sum(last_v)

    t = v
    t.reverse()
    last_v = [v[-1]]
    while not np.all((t := np.diff(t))[:] == 0):
        last_v.append(t[-1])

    total[0] += sum(last_v)

print(total)
