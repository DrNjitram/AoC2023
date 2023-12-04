cards = [[id, [{int(section) for section in no.split(" ") if section != ''} for no in card.split(": ")[1].split(" | ")]] for id, card in enumerate([line.strip() for line in open("input/d4")])]

part1 = 0
copies = [1 for _ in cards]
for id, (winning, numbers) in cards:
    print(id)
    winnings = winning & numbers

    part1 += int(2**(len(winnings)-1))
    for i in range(len(winnings)):
        copies[id+i+1] += copies[id]

print(part1)
print(sum(copies))