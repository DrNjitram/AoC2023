from collections import defaultdict


def print_dict(state: dict, chars: tuple = ("#", ".")):
    print("Field:")
    x_s, y_s = zip(*list([k for k, v in state.items() if v]))
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            line += chars[0] if state[(x, y)] else chars[1]
        print(line)


def print_dict_mapped(state: defaultdict, chars: tuple = ("#", ".")):
    print("Field:")
    x_s, y_s = zip(*list([k for k, v in state.items() if v]))
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            line += chars[state[(x, y)]]
        print(line)


def print_list(state: list, chars: tuple = ("#", ".")):
    print("Field:")
    x_s, y_s = [set(l) for l in zip(*state)]
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            line += chars[0] if [x, y] in state else chars[1]
        print(line)


def dist(p2, p1, p0) -> float:
    x2, y2, _ = p2
    x1, y1, _ = p1
    x0, y0 = p0
    return abs((x2 - x1) * (y2 - y1) - (x1 - x0) * (y2 - y1)) / np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_closes_color(poly, p) -> None | str:
    distance = []
    colors = []
    for i in range(len(poly)):
        colors.append(poly[i][2])
        d = dist(poly[i - 1], poly[i], p)
        distance.append(d)

    m = max(distance)
    if distance.count(m) == 1:
        return colors[distance.index(max(distance))]
    else:
        return None


def point_inside(poly, p) -> bool:
    x, y = p
    c = False
    for i in range(len(poly)):
        x2, y2, _ = poly[i - 1]
        x1, y1, _ = poly[i]
        if dist(poly[i - 1], poly[i], p) == 0:
            return True
        if (((y1 <= y < y2) or
             (y2 <= y < y1)) and
                (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1)):
            c = not c
    return c
