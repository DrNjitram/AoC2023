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



print(get_combos([2, 2, 1, 1] ))
