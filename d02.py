lines = [line.strip() for line in open("input/d2").readlines()]

# rgb
valid = {"red": 12, "green": 13,"blue": 14}

sum_id = 0
power_sum = 0
for i, line in enumerate(lines):
    rgb = {"red": 0, "green": 0, "blue": 0}
    bag = [[c.split(" ") for c in cubes.split(", ")] for cubes in line.split(": ")[1].split("; ")]
    possible = True
    for grab in bag:
        for p, c in grab:
            rgb[c] = max(int(p), rgb[c])
            if valid[c] < int(p):
                possible = False

    if possible: sum_id += i + 1
    power_sum += rgb["red"] * rgb["green"] * rgb["blue"]

print(sum_id)
print(power_sum)


