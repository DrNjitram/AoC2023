import re
import math
import time

start_time = time.time()
field = [line.strip() for line in open("input/day3_big.txt")]


numbers = []
gears = []
all_parts = {}

id = 0
for y, line in enumerate(field):
    print(line)
    part_result = re.findall(r"\d*", line)
    for x, val in enumerate(part_result):
        if val != '':
            x_pos = sum([1 if a == '' else len(a) for a in part_result[:x]])
            val = int(val)
            positions = [(x_pos + i, y) for i in range(int(math.log(val, 10)) + 1)]
            numbers.append((val, positions))
            for pos in positions:
                all_parts[pos] = (val, id)
            id += 1

parts = 0
for val, pos in numbers:
    valid = False
    for x, y in pos:
        for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [1, 0], [0, -1], [0, 1]]:
            if 0 <= x + dx < len(field[0]) and 0 <= y + dy < len(field) and not field[y + dy][x + dx].isdigit() and not \
                    field[y + dy][x + dx] == ".":
                valid = True
    if valid:
        parts += val

print(parts)
ratios = 0
all_positions = list(all_parts.keys())
for y, line in enumerate(field):
    for x, c in enumerate(line):
        if c == "*":
            parts = []
            ids = []
            for dx, dy in [[-1, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [1, 0], [0, -1], [0, 1]]:
                if (x+dx, y+dy) in all_positions:
                    val, id = all_parts[(x+dx, y+dy)]
                    if id not in ids:
                        parts.append(val)
                        ids.append(id)

            if len(parts) == 2:
                ratios += parts[0]*parts[1]

print(ratios)
print(time.time()-start_time)