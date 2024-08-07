def simple(num):
    if num == 2:
        return True
    if num == 0 and num == 1 and not num % 2:
        return False
    for dev in range(3, int(num ** 0.5) + 1, 2):
        if not num % dev:
            return False
    return True

#number = int(input('Введите число: '))
number = 103
print (simple(number))

