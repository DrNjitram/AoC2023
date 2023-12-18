def find_plane(b: list[str], horizontal: bool, delta_limit) -> tuple[int, int]:
    for y in range(1, len(b)):
        l = min(y, len(b) - y)

        deltas = 0
        for s1, s2 in zip(b[:y][::-1][:l], b[y:y + l]):
            for c1, c2 in zip(s1, s2):
                if c1 != c2:
                    deltas += 1

        if deltas == delta_limit:
            return y, horizontal

    return find_plane(list(zip(*b)), False, limit)


blocks = [block.split("\n") for block in open("input/d13").read().split("\n\n")]

for limit in [0, 1]:
    ans = sum([[mirror * 100 if plane else mirror for mirror, plane in [find_plane(block, True, limit)]][0] for block in blocks])
    print(ans)
