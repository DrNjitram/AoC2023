import numpy as np

blocks = open("input/d5").read().split("\n\n")
seeds = [int(v) for v in blocks[0].split(": ")[1].split(" ")]


def apply_map_part1(seeds, ranges):
    output = []

    for seed in seeds:
        for d, s, r in ranges:
            if s <= seed < s + r:
                output.append(seed - s + d)
                break
        else:
            output.append(seed)
    return output


def apply_map_part2(seeds, ranges):
    output = []

    i = 0
    while i < len(seeds):
        seed_s, seed_r = seeds[i]
        for j, (d, s, r) in enumerate(ranges):
            if s <= seed_s < s + r:
                if seed_s + seed_r < s + r:
                    output.append([seed_s - s + d, seed_r])
                    break
                else:
                    output.append([seed_s - s + d, s+r-seed_s])
                    seeds.append([s+r, seed_r - (s + r - seed_s)])
                    break
        else:
            output.append(seeds[i])
        i += 1

    return output


maps = []
for block in blocks[1:]:
    lines = block.split("\n")
    ranges = np.zeros([len(lines) - 1, 3])
    for i, line in enumerate(lines[1:]):
        ranges[i, :] = np.array([int(v) for v in line.split(" ")])

    maps.append(ranges[ranges[:, 1].argsort()])

seeds1 = seeds.copy()
for m in maps:
    seeds1 = apply_map_part1(seeds1, m)
print("Part 1", min(seeds1))

seeds2 = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
for m in maps:
    seeds2 = apply_map_part2(seeds2, m)
print("Part 2", min([s for s, r in seeds2]))
