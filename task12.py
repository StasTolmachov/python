def find_numbers(S, P):
    for X in range(1, 1001):
        for Y in range(X, 1001):  # начинаем с X, чтобы избежать повторений
            if X + Y == S and X * Y == P:
                return X, Y
    return None, None

# Тестирование:
print(find_numbers(5, 6))  # (2, 3)
