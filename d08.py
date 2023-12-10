import math

ds, n = open("input/d8").read().strip().split("\n\n")

paths = dict()
for p in n.split("\n"):
    s, e = p.split(" = ")
    paths[s] = tuple(e[1:-1].split(", "))

current = [n for n in paths.keys() if n.endswith("A")]
sorted(current)
l = []
AAA = None
steps = 0
while len(current) > 0:
    d = ds[steps % len(ds)]
    steps += 1
    current = [paths[c][0] if d == "L" else paths[c][1] for c in current]
    for c in current:
        if c.endswith("Z"):
            if current.index(c) == 0 and AAA is None:
                AAA = steps
            l.append(steps)
            current.remove(c)


print("Part 1:", AAA)
print("Part 2:", math.lcm(*l))
