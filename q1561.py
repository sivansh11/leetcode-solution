def maxCoins(piles: list[int]) -> int:
    piles.sort(reverse=True)
    sum = 0
    for i in range(int(len(piles) / 3)):
        sum += piles[i * 2 + 1]
    return sum


assert maxCoins([2, 4, 1, 2, 7, 8]) == 9
assert maxCoins([2, 4, 5]) == 4
assert maxCoins([9, 8, 7, 6, 5, 1, 2, 3, 4]) == 18
