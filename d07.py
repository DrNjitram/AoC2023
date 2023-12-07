import functools

hands = [line.strip().split() for line in open("input/d7")]


def get_strength1(hand: list) -> int:
    hand, bet = hand
    strength_string = ""

    unique = list(set(hand))
    match len(unique):
        case 1:  # Five of a kind
            strength_string += "7"
        case 2:  # Four of a kind or Full House
            if any(hand.count(c) == 4 for c in unique):
                strength_string += "6"
            else:
                strength_string += "5"
        case 3:  # Three of a kind or 2 pair
            if any(hand.count(c) == 3 for c in unique):
                strength_string += "4"
            else:
                strength_string += "3"
        case 4:  # One pair
            strength_string += "2"
        case 5:
            strength_string += "1"

    for c in hand:
        strength_string += "14" if c == 'A' else "13" if c == "K" else "12" if c == "Q" else "11" if c == "J" else "10" if c == "T" else '0' + c

    return int(strength_string)


def get_strength2(hand: list) -> int:
    hand, bet = hand
    strength_string = ""

    unique = list(set(hand))
    match len(unique):
        case 1:  # Five of a kind
            strength_string += "7"
        case 2:  # Four of a kind or Full House
            if 'J' in unique:
                strength_string += "7"
            elif any(hand.count(c) == 4 for c in unique):
                strength_string += "6"  # Four of a kind
            else:
                strength_string += "5"  # Full House
        case 3:  # Three of a kind or 2 pair
            if any(hand.count(c) == 3 for c in unique):
                if 'J' in unique:  # Four of a kind
                    strength_string += "6"
                else:  # Three of a kind
                    strength_string += "4"
            else:
                if hand.count("J") == 2:  # Four of a kind JJAAB
                    strength_string += "6"
                elif hand.count("J") == 1:  # Full House AABBJ
                    strength_string += "5"
                else:  # Two pair
                    strength_string += "3"
        case 4:  # One pair
            if "J" in unique:  # Three of a kind AABCJ or JJABC -> AAABC
                strength_string += "4"
            else:
                strength_string += "2"
        case 5:
            if 'J' in unique:
                strength_string += "2"
            else:
                strength_string += "1"

    for c in hand:
        strength_string += "14" if c == 'A' else "13" if c == "K" else "12" if c == "Q" else "01" if c == "J" else "10" if c == "T" else '0' + c

    return int(strength_string)


print("Part 1", sum([(i + 1) * int(b) for i, (_, b) in enumerate(sorted(hands, key=get_strength1))]))
print("Part 2", sum([(i + 1) * int(b) for i, (_, b) in enumerate(sorted(hands, key=get_strength2))]))
