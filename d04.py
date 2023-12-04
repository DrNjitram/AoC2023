cards = [line.strip() for line in open("input/d4")]
cards = [[id, [{int(section) for section in no.split(" ") if section != ''} for no in card.split(": ")[1].split(" | ")]] for id, card in enumerate(cards)]
original_length = len(cards)

part1 = 0
i = 0
while i < len(cards):
    id, (winning, numbers) = cards[i]
    print(i, id)
    winnings = winning & numbers

    if i < original_length: part1 += 2**(len(winnings)-1)
    cards += cards[id+1:min(original_length, id+len(winnings)+1)]

    i += 1

print(part1)
print(len(cards))