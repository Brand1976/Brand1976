# Сумма цифр в числе, пока не получится однозначное число

num = input('Введите целое число: ')
print(num)
while int(num) > 9:
    sum = 0
    for i in str(num):
        sum += int(i)
    num = sum
print('Ответ: ', num)
