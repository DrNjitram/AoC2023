def roll(state: list, left: bool) -> list:
    compact = []
    for line in state:
        line = list(line)[::1 if left else -1]
        move = True
        while move:
            move = False
            for i in range(len(line) - 1):
                if line[i] == "." and line[i + 1] == "O":
                    line[i] = "O"
                    line[i + 1] = "."
                    move = True

        compact.append(line[::1 if left else -1])
    return compact


def cycle(state: list, c: int) -> list:
    # N, W, S, E
    state = list(zip(*state))  # transpose
    state = roll(state, True)  # Roll North
    if c == 1:
        print("Part 1", get_load(list(zip(*state))))
    state = list(zip(*state))  # transpose
    state = roll(state, True)  # Roll West
    state = list(zip(*state))  # transpose
    state = roll(state, False)  # Roll South
    state = list(zip(*state))  # transpose
    state = roll(state, False)  # Roll East
    return ["".join(l) for l in state]


def get_load(state: list) -> int:
    state = list(zip(*state))
    load = 0
    for line in state:
        for i, c in enumerate(line):
            if c == 'O':
                load += len(line) - i
    return load


rocks = [line.strip() for line in open("input/d14")]

memoization = {"".join(rocks): (get_load(rocks), 0)}
rev = []
c = 0
target = 1000000000
while c < target:
    c += 1
    rocks = cycle(rocks, c)
    rev.append(get_load(rocks))
    if "".join(rocks) not in memoization:
        memoization["".join(rocks)] = (rev[-1], c)
    else:
        break

cycle_start = memoization["".join(rocks)][1]
in_c = (target - cycle_start) % (c - cycle_start)

print("Part 2", rev[cycle_start + in_c-1])
