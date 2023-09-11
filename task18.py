def closest_number(arr, X):
    return min(arr, key=lambda num: abs(num - X))

# Тестирование:
N = 5
A = [1, 2, 3, 4, 5]
X = 6
print(closest_number(A, X))  # 5
