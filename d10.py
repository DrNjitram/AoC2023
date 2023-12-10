from collections import defaultdict

from numpy import real, imag

def print_gol(state: dict):
    print("Field:")
    x_s, y_s = zip(*list([[int(real(k)), int(imag(k))] for k,v in state.items() if v]))
    for y in range(min(y_s), max(y_s) + 1):
        line = ""
        for x in range(min(x_s), max(x_s) + 1):
            line += str(state[y*1j + x]) if y*1j + x in state else "."
        print(line)


field = [line.strip() for line in open("input/d10")]

print(field)

nodes = [a for a in [[(x, y) for x, c in enumerate(l) if c == "S"] for y, l in enumerate(field)] if a != []][0]
nodes = [nodes[0][0] + nodes[0][1] *1j]

adj = [-1, 1, -1j, 1j]
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

distances = {nodes[0]: 0}

while len(nodes) > 0:
    next_nodes = []
    for coord in nodes:
        curr_symbol = field[int(imag(coord))][int(real(coord))]
        for dcoord in adj:
            next_node = coord + dcoord
            if next_node not in distances and 0 <= real(next_node) < len(field[0]) and 0 <= imag(next_node) < len(field):
                next_symbol = field[int(imag(next_node))][int(real(next_node))]
                if next_symbol != ".":
                    if len({dcoord} & connections_to[curr_symbol] & connections_from[next_symbol]) > 0:
                        next_nodes.append(next_node)
                        distances[next_node] = distances[coord] + 1

    nodes = next_nodes

#    print(next_nodes)
#    print_gol(distances)

print(max(distances.values()))