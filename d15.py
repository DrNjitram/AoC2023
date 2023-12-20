from collections import defaultdict


def parse_hash(string: str) -> tuple:
    v = 0
    for i, h in enumerate(string):
        if h in ["=", "-"]:
            lbl = string[:i]
            lns = 0 if '-' in string else int(string[i + 1:])
            bx = v

        v += ord(h)
        v *= 17
        v %= 256

    return v, bx, lbl, lns


weed = open("input/d15").read().strip().split(",")

p1 = p2 = 0
boxes = defaultdict(dict)
for h in weed:
    p1d, box, label, lens = parse_hash(h)
    p1 += p1d

    if lens:
        boxes[box][label] = int(lens)
    else:
        if label in boxes[box]:
            boxes[box].pop(label)

for box, lenses in boxes.items():
    for i, focal in enumerate(lenses.values()):
        p2 += (box+1)*(i+1)*focal

print("Part 1:", p1)
print("Part 2:", p2)
