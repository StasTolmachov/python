def can_break_chocolate(n, m, k):
    return k < n * m and (k % n == 0 or k % m == 0)


# Тестирование
print(can_break_chocolate(3, 2, 3))  # True
print(can_break_chocolate(3, 2, 1))  # False
