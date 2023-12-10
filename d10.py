from numpy import real, imag


def p1(nodes):
    distances = {nodes[0]: 0}
    adj = [1, -1, -1j, 1j]

    while len(nodes) > 0:
        next_nodes = []
        for coord in nodes:
            curr_symbol = field[int(imag(coord))][int(real(coord))]
            for dcoord in adj:
                next_node = coord + dcoord
                if next_node not in distances and 0 <= real(next_node) < len(field[0]) and 0 <= imag(next_node) < len(
                        field):
                    next_symbol = field[int(imag(next_node))][int(real(next_node))]
                    if next_symbol != ".":
                        if len({dcoord} & connections_to[curr_symbol] & connections_from[next_symbol]) > 0:
                            next_nodes.append(next_node)
                            distances[next_node] = distances[coord] + 1

        nodes = next_nodes

    return distances


def move_inbetween(next_coord, direction, field) -> bool:
    f, t = [next_coord + direction * 1j, next_coord + direction * -1j]

    curr_symbol = field[int(imag(f))][int(real(f))]
    next_symbol = field[int(imag(t))][int(real(t))]
    return "." in [curr_symbol, next_symbol] or len({direction * -2j} & connections_to[curr_symbol] & connections_from[next_symbol]) == 0


field = [line.strip() for line in open("input/d10")]

nodes = [a for a in [[(x, y) for x, c in enumerate(l) if c == "S"] for y, l in enumerate(field)] if a != []][0]
nodes = [nodes[0][0] + nodes[0][1] * 1j]

connections_to = {
    "S": {-1j, 1j, -1, 1},
    "|": {-1j, 1j},
    "-": {-1, 1},
    "L": {1, -1j},
    "J": {-1, -1j},
    "7": {-1, 1j},
    "F": {1, 1j}
}
connections_from = {
    "S": {-1j, 1j, -1, 1},
    "|": {1j, -1j},
    "-": {1, -1},
    "L": {-1, 1j},
    "J": {1, 1j},
    "7": {1, -1j},
    "F": {-1, -1j}
}

distances_p1 = p1(nodes)
print(max(distances_p1.values()))

possible = []

x_s, y_s = zip(*list([[int(real(k)), int(imag(k))] for k, v in distances_p1.items() if v]))
for y in range(min(y_s), max(y_s) + 1):
    for x in range(min(x_s), max(x_s) + 1):
        if y * 1j + x not in distances_p1:
            possible.append(y * 1j + x)

adj = [-0.5, 0.5, -0.5j, 0.5j]
known = dict()

for p in possible:
    state = 1
    if p not in known:
        curr = [p]
        nodes = [p]
        while len(nodes) > 0:
            next_nodes = []
            for coord in nodes:
                for dcoord in adj:
                    next_node = coord + dcoord
                    if not (0 <= real(next_node) <= len(field[0]) - 1 and 0 <= imag(next_node) <= len(field) - 1):
                        state = 0
                    elif (imag(next_node).is_integer() and real(
                            next_node).is_integer() and next_node not in distances_p1) or move_inbetween(next_node,
                                                                                                         dcoord, field):
                        if next_node not in curr:
                            next_nodes.append(next_node)
                            curr.append(next_node)

            nodes = next_nodes

        for c in curr:
            known[c] = state

print(len([(k, v) for k, v in known.items() if
           v == 1 and imag(k).is_integer() and real(k).is_integer() and k not in distances_p1.keys()]))
