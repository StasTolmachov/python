def max_berries(bushes):
    n = len(bushes)
    max_sum = 0

    for i in range(n):
        # Выберем три куста: текущий, предыдущий и следующий
        total = bushes[i] + bushes[(i-1) % n] + bushes[(i+1) % n]
        if total > max_sum:
            max_sum = total

    return max_sum

# Тестирование:
N = int(input())
bushes = [int(input()) for _ in range(N)]

print(max_berries(bushes))
