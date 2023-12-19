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
