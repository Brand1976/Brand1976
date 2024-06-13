num = input('Введите число: ')
count = num.count('.')
#print(count)
if count > 1: print('Число не является вещественным')
else:
    if float(num) > 0: print('Это положительное вещественное число')
    elif float(num) < 0: print('Это отрицательное вещественное число')
    else: print('Это "0"')
