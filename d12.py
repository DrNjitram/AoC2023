def combinations(springs: str, damaged: int) -> int:
    pass


records = [line.strip().split(" ") for line in open("input/d12_test")]

p1 = 0
for spring, record in records:
    record = [int(no) for no in record.split(",")]
    spring = [section for section in spring.split(".") if section != '']

    perms = 1
    if len(record) == len(spring) and all([r <= len(s) for r, s in zip(record, spring)]):
        perms *= [combinations(s, r) for r, s in zip(record, spring)]

        # fails on ???.?? 1,1
    else:
        pass

    print(spring, record)
    print(perms)
