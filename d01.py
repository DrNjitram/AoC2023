print(sum([int(l[0] + l[-1]) for l in [[c for c in line.strip() if c.isdigit()] for line in open(r"input\d1").readlines()]]))
print(sum([int(l[0] + l[-1]) for l in ["".join([c if c.isdigit()else str([line[i:].startswith(d) for d in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']].index(True)) if any([line[i:].startswith(d) for d in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]) else '' for i, c in enumerate(line.strip())]).strip()for line in open(r"input\d1").readlines()]]))

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
s = 0
for line in [l.strip() for l in open(r"input\d1").readlines()]:
    vals = []
    for i in range(len(line)):
        if line[i].isdigit():
            vals.append(int(line[i]))
        else:
            for val, no in enumerate(numbers):
                if line[i:].startswith(no):
                    vals.append(val)

    s += vals[0] * 10 + vals[-1]

print(s)

