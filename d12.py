import math
import re


def combinations(spring: str, damaged: tuple) -> int:
    print(spring, damaged)
    if len(spring) == sum(damaged) + len(damaged) - 1:
        return 1
    elif len(damaged) == 1:
        return len(spring) - damaged[0] + 1
    elif len(damaged) == 2:
        s, e = damaged
        return sum(len(spring[i + s + 1:]) - e + 1 for i in range(0, len(spring) - sum(damaged) + 1))
    else:
        return sum(
            combinations(spring[i+damaged[0]:], damaged[1:]) for i in range(0, len(spring) - sum(damaged[1:]) + 1)
        )


def cleanup(s: list, r: list) -> tuple[list[str], list[int]]:
    try:
        while True:
            if "#" in s[0] and len(s[0]) == r[0]:
                s.pop(0)
                r.pop(0)
            else:
                break
        while True:
            if "#" in s[-1] and len(s[-1]) == r[-1]:
                s.pop(-1)
                r.pop(-1)
            else:
                break
    except IndexError as e:
        pass

    return s, r


def s_e_quest(s: str) -> tuple:
    l = len(s)
    return l - len(s.lstrip("?")), l - len(s.rstrip("?"))


def reduce(s: list, r: list) -> tuple | int:
    if len(s) == 0:
        return 1
    if len(s) > 0:
        if len(r) == 1 and len(s) == 1:
            if "#" not in s[0]:
                return len(s[0]) - r[0] + 1
            elif r[0] * "#" in s[0]:
                return 1
            else:
                return s, r
        elif len(r) == len(s) and all([r2 - len(s2) in [0, -1] for r2, s2 in zip(r, s)]):
            return sum(len(s2) - r2 + 1 for r2, s2 in zip(r, s))
        elif len(s) == 1 and (sum(r) + len(r) - 1) - (
                len(s[0]) - sum(s_e_quest(s[0]))) <= 2:
            return 1
        elif len(s) == 1 and (sum(r) + len(r) - 1) == len(s[0]):
            return 1
        else:
            if len(s) == 1:
                sorted_record = sorted(r, reverse=True)
                for sr in sorted_record:
                    fs = "#" * sr
                    if fs in s[0]:
                        r = [r2 for r2 in r if r2 != sr]
                        s = [s for s in re.split(f'\\??{fs}\\??', s[0]) if len(s) > 1]
    return s, r


def get_options(s: list, n: int) -> list:
    if n == len(s):
        return [s]
    if n == 1:
        return [[s2] for s2 in s]
    options = []
    for i in range(0, len(s) - n + 1):
        options += [[s[i]] + o for o in get_options(s[i + 1:], n - 1)]
    return options


def get_combos(r: list) -> tuple | set:
    if len(r) == 2:
        return (tuple([tuple(r)])), (tuple([tuple([r[0]]), tuple([r[1]])]))
    if len(r) == 1:
        return tuple([tuple(r)])
    combos = set()
    for n in range(2, len(r) + 1):
        for i in range(0, len(r) - n + 1):
            sub_r = tuple([tuple(r[i:i + n])])
            if i > 0:
                start_combo = get_combos(r[:i])
                sub_r = tuple(s + sub_r for s in start_combo)
                if i < len(r) - n:
                    end_combo = get_combos(r[i + n:])
                    sub_r = tuple(sub_r[0] + s for s in end_combo)
            elif i < len(r) - n:
                end_combo = get_combos(r[i + n:])
                sub_r = tuple(sub_r + s for s in end_combo)
            if n == len(r):
                sub_r = tuple([sub_r])
            combos.update(sub_r)
    return combos


records = [line.strip().split(" ") for line in open("input/d12_test")]
#records = [line.strip().split(" ") for line in ["?#...??????.??.?.# 2,2,2,1,1,1"]]

p1 = 0
for spring, record in records:
    record = [int(no) for no in record.split(",")]
    spring = [section for section in spring.split(".") if section != '']

    spring, record = cleanup(spring, record)
    if spring[0].startswith("#"):
        spring[0] = spring[0][record.pop(0):]
    if spring[-1].endswith("#"):
        spring[-1] = spring[-1][:-record.pop(-1) - 1]

    spring = [s for s in spring if len(s) > 0]

    perms = 0

    while True:
        ans = reduce(spring, record)
        if type(ans) is int:
            perms = ans
            break
        elif spring != ans[0] and record != ans[1]:
            spring, record = ans
        else:
            break

    if not perms:
        if len(record) == 2 and "#" not in "".join(spring):
            flag = False
            s, e = record
            for spr in spring:
                if len(spr) > s + e + 1:
                    for i in range(0, len(spr) - e - s + 1):
                        perms += len(spr[i + s + 1:]) - e + 1
                else:
                    flag = True
                print(perms)
            if flag:
                options = get_options(spring, 2)
                for a, b in options:
                    if len(a) >= s and len(b) >= e:
                        perms += (len(a) - s + 1) * (len(b) - e + 1)
                # [1, 4] ['???', '???????'] 12 + 3
        else:
            all_combos = get_combos(record)
            all_combos.update(tuple([tuple([tuple([r]) for r in record])]))
            all_options = [get_options(spring, n) for n in range(1, len(spring) + 1)]

            #print(all_options)
            for c in all_combos:
                if (len(c) == 1 and len(spring) > 1) or len(c) > len(spring):
                    continue
                c = tuple(sc if type(sc) is tuple else tuple([sc]) for sc in c)

                opts = all_options[len(c) - 1]
                for o in opts:
                    if all(sum(sc) + len(sc) - 1 <= len(so) for so, sc in zip(o, c)):
                        perms += math.prod([combinations(so, sc) for so, sc in zip(o, c)])
                        print(c, o, perms)

            if len(record) <= len(spring):
                options = get_options(spring, len(record))
                for opt in options:
                    if all(len(s) >= r for s, r in zip(opt, record)):
                        perms += math.prod([len(s) - r + 1 for s, r in zip(opt, record)])
                        print(opt, perms)
            # combinatrics
            print(record, spring, perms)
            

    print(record, spring, perms)
    p1 += perms

print("Part 1:", p1)
