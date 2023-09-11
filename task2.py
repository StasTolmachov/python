number = 12345
arrStr = []
result = 0


# for itemStr in str(number):
#     arrStr += itemStr

# for itemStr in arrStr:
#     result += int(itemStr)

# print(result)


def sumOfDigits(number):
    return sum(int(itemStr) for itemStr in str(number))


print(sumOfDigits(number))
