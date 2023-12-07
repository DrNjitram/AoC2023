def get_wins(races):
    wins = 1
    for t, d in races:
        w = 0
        for speed in range(1, t - d // (t - 1)):
            if speed * (t - speed) > d:
                w += 1
        wins *= w
    return wins


print(get_wins([[41, 249], [77, 1362], [70, 1127], [96, 1011]]))
print(get_wins([[41777096, 249136211271011]]))
