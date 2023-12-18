import itertools

galaxy = [line.strip() for line in open("input/d11")]

stars = []
for y, line in enumerate(galaxy):
    for x, c in enumerate(line):
        if c == "#":
            stars.append([x, y])

xs, ys = [list(set(l)) for l in zip(*stars)]


def expand(state: list, factor: int) -> int:
    expanded_state = [[sx + (factor - 1) * (sx - sum([1 for x in xs if x < sx])),
                       sy + (factor - 1) * (sy - sum([1 for y in ys if y < sy]))] for sx, sy in
                      state]
    return sum([abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in itertools.combinations(expanded_state, 2)])


print(expand(stars, 2))
print(expand(stars, 1000000))
