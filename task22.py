def find_common_elements(set1, set2):
    return sorted(list(set(set1) & set(set2)))

# Тестирование:
n = int(input())
set1 = [int(input()) for _ in range(n)]
m = int(input())
set2 = [int(input()) for _ in range(m)]

result = find_common_elements(set1, set2)
for num in result:
    print(num)
