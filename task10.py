def min_flips(coins):
    heads = coins.count('H')
    tails = coins.count('T')
    return min(heads, tails)

# Тестирование:
print(min_flips(['H', 'T', 'H', 'T']))  # 2
