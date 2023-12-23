def get_area(poly):
    area = 0
    for i in range(len(poly)):
        px, py = poly[i - 1]
        cx, cy = poly[i]
        area += px * cy - py * cx

    area = abs(area / 2)

    for i in range(len(poly)):
        px, py = poly[i - 1]
        cx, cy = poly[i]
        area += (abs(px - cx) + abs(py - cy)) / 2

    return area + 1


def add(L, D, p):
    x, y = p
    match D:
        case "R":
            return x + L, y
        case "D":
            return x, y - L
        case "U":
            return x, y + L
        case "L":
            return x - L, y


lines = [line.strip() for line in open("input/d18")]

polygon1 = [(0, 0)]
polygon2 = [(0, 0)]
for line in lines:
    D, L, C = line.split()
    L = int(L)

    polygon1.append(add(L, D, polygon1[-1]))

    match C[7]:
        case "0":
            D = "R"
        case "1":
            D = "D"
        case "2":
            D = "L"
        case _:
            D = "U"

    polygon2.append(add(int("0x" + C[2:7], 0), D, polygon2[-1]))

polygon1 = polygon1[1:]
polygon2 = polygon2[1:]

print(get_area(polygon1))
print(get_area(polygon2))
