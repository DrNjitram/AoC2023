import math
import re


def combinations(spr: str, damaged: tuple|list) -> int:
    spr, damaged = cleanup([spr], list(damaged))
    if len(damaged) == 0:
        return 1
    spr = spr[0]

    print(spring, damaged)
    if len(spr) == sum(damaged) + len(damaged) - 1:
        return 1
    elif len(damaged) == 1:
        if "#" in spr:
            if spr.startswith("#") or spr.endswith("#"):
                return 1
            if spr.count("#") == damaged[0]:
                return 1
            else:
                return sum(1 for i in range(len(spr)-damaged[0]+1) if spr[i:i+damaged[0]].count("#") == spr.count("#"))
        else:
            return len(spr) - damaged[0] + 1
    elif len(damaged) == 2:
        s, e = damaged
        if "#" in spr:
            if spr.startswith("#"):
                if spr.endswith("#"):
                    return 1
                else:
                    return combinations(spr[s+1:], (e))
            if spr.endswith("#"):
                return combinations(spr[:e-1], (s))
            if spr.count("#") == s+e:
                return 1
            else:
                return sum(sum(1 for j in range(i+s+1, len(spr)-e+1) if spr[j:j+e].count("#")+spr[i:i + s].count("#") == spr.count("#")) for i in range(0, len(spr) - sum(damaged) + 1))
        else:
            return sum(len(spr[i + s + 1:]) - e + 1 for i in range(0, len(spr) - sum(damaged) + 1))
    else:
        sums = []
        for i in range(0, len(spr) - sum(damaged[1:]) - len(damaged) + 1):
            sums.append(combinations(spr[i + damaged[0]+1:], damaged[1:]))
        print(spr, damaged, sums)
        if 0 in sums:
            return 0
        else:
            return sum(sums)


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

        if s[0].startswith("#"):
            s[0] = s[0][r.pop(0):]
        if s[-1].endswith("#"):
            s[-1] = s[-1][:-r.pop(-1) - 1]
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
                    else:
                        break
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


records = [line.strip().split(" ") for line in open("input/d12")]
records = [line.strip().split(" ") for line in [".????#??????#?#??? 1,5,1,1,1,1"]]

p1 = 0
for index, (spring, record) in enumerate(records):
    record = [int(no) for no in record.split(",")]
    spring = [section for section in spring.split(".") if section != '']

    spring, record = cleanup(spring, record)


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
                #print(perms)
            if flag:
                options = get_options(spring, 2)
                for a, b in options:
                    if len(a) >= s and len(b) >= e:
                        perms += (len(a) - s + 1) * (len(b) - e + 1)
                # [1, 4] ['???', '???????'] 12 + 3
        else:
            if len(spring) == 1:
                perms = combinations(spring[0], record)
            else:
                all_combos = get_combos(record)
                if type(all_combos) == tuple:
                    if len(all_combos) == 1:
                        all_combos = set(tuple([all_combos]))
                    else:
                        all_combos = set(all_combos)
                else:
                    all_combos.update(tuple([tuple([tuple([r]) for r in record])]))
                all_options = [get_options(spring, n) for n in range(1, len(spring) + 1)]


                #print(all_options)
                for c in all_combos:
                    if (len(c) == 1 and len(c[0]) == 1 and len(spring) > 1) or len(c) > len(spring):
                        if len(c) == 1 and len(c[0]) == 1 :
                            perms += sum([combinations(o, c[0]) for o in spring])
                        #print(c, spring, perms)

                    else:
                        c = tuple(sc if type(sc) is tuple else tuple([sc]) for sc in c)

                        opts = all_options[len(c) - 1]
                        for o in opts:
                            hsh_valid = False
                            for so, sc in zip(o, c):
                                hsh = len(so)
                                while hsh > 0:
                                    if hsh*"#" in so:
                                        break
                                    hsh -= 1
                                for ssc in sc:
                                    if ssc >= hsh:
                                        hsh_valid = True
                                if not hsh_valid:
                                    break
                            if hsh_valid and (sum(so.count("#") for so in o) == sum(s.count("#") for s in spring) and
                                    all(sum(sc) + len(sc) - 1 <= len(so) for so, sc in zip(o, c))):
                                perms += math.prod([combinations(so, sc) for so, sc in zip(o, c)])
                                print(c, o, perms)

            # combinatrics
            #print(record, spring, perms)


    print(index, record, spring, perms)
    if perms <0:
        raise Exception
    p1 += perms


print("Part 1:", p1)
