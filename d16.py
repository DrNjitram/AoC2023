import numpy as np


def get_symbol(g: list, c: complex):
    return g[int(np.imag(c))][int(np.real(c))]


def in_bounds(g: list, c: complex):
    return 0 <= np.real(c) < len(g[0]) and 0 <= np.imag(c) < len(g)


def visited_before(g: list, visited: dict[tuple[complex, complex], int], position: tuple[complex, complex]):
    p, o = position
    if position in visited:
        return True
    if get_symbol(g, p) in [".", "|", "-"]:
        return (p, o * -1) in visited
    return False


def is_horizontal(position: complex):
    return True if position in [-1 + 0j, 1 + 0j] else False


def get_next(grid: list[str], position: tuple[complex, complex]) -> list[tuple[complex, complex]]:
    pos, orientation = position
    c = get_symbol(grid, pos)

    if is_horizontal(orientation):
        match c:
            case "." | "-":
                return [(pos + orientation, orientation)]
            case "|":
                return [(pos + orientation * 1j, orientation * 1j), (pos + orientation * -1j, orientation * -1j)]
            case "\\":
                return [(pos + orientation * 1j, orientation * 1j)]
            case "/":
                return [(pos + orientation * -1j, orientation * -1j)]
    else:
        match c:
            case "." | "|":
                return [(pos + orientation, orientation)]
            case "-":
                return [(pos + orientation * 1j, orientation * 1j), (pos + orientation * -1j, orientation * -1j)]
            case "\\":
                return [(pos + orientation * -1j, orientation * -1j)]
            case "/":
                return [(pos + orientation * 1j, orientation * 1j)]


def get_energized(grid, to_visit):
    visited_tiles = dict()

    while len(to_visit):
        pos = to_visit.pop(0)
        if in_bounds(grid, pos[0]) and not visited_before(grid, visited_tiles, pos):
            visited_tiles[pos] = 1
            to_visit += get_next(grid, pos)

    return len(set([p for p, _ in visited_tiles.keys()]))


grid = [line.strip() for line in open("input/d16")]

print("Part 1:", get_energized(grid, [(0 + 0j, 1 + 0j)]))

energized = []
for a in range(len(grid)):
    energized.append(get_energized(grid, [(0 + a * 1j, 1 + 0j)]))
    energized.append(get_energized(grid, [(len(grid[0]) - 1 + a * 1j, -1 + 0j)]))

for a in range(len(grid[0])):
    energized.append(get_energized(grid, [(a + 0j, 0 + 1j)]))
    energized.append(get_energized(grid, [(a + len(grid) - 1 * 1j, 0 - 1j)]))

print("Part 2:", max(energized))
