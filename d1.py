print(sum([int(l[0] + l[-1]) for l in
           [[c for c in line.strip() if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']] for line in
            open(r"input\d1").readlines()]]))

numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
s = 0
for line in [l.strip() for l in open(r"input\d1").readlines()]:
    vals = []
    for i in range(len(line)):
        if line[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            vals.append(int(line[i]))
        for val, no in enumerate(numbers):
            if line[i:].startswith(no):
                vals.append(val + 1)

    s += vals[0] * 10 + vals[-1]

print(s)
