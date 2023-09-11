a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разницу прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

def arithmetic_progression(a1, d, n):
    return [a1 + (i-1)*d for i in range(1, n+1)]

print(arithmetic_progression(a1, d, n))
