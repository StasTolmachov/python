numbers = list(map(int, input("Введите элементы массива через пробел: ").split()))
min_value = int(input("Введите минимум диапазона: "))
max_value = int(input("Введите максимум диапазона: "))

def find_indices_in_range(numbers, min_value, max_value):
    return [index for index, value in enumerate(numbers) if min_value <= value <= max_value]

print(find_indices_in_range(numbers, min_value, max_value))
