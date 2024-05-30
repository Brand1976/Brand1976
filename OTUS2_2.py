#Вариант 1
cinema = [[1,0,1,0,1,1],[1,1,0,0,1,0,],[0,0,0,1,1,0],[1,0,0,0,0,1],[1,0,0,0,0,0]]
tickets = input('Введите количество билетов: ')
row_num = -1
for row in cinema:
    free = 0
    for place in row:
        if place == 0:
            free += 1
            if free == int(tickets):
                row_num = cinema.index(row)
                break
        else:
            free = 0
    if row_num != -1:
        break
else:
    row_num = False
print('Номер ряда: ', row_num)

#Вариант 2
cinema = [[1,0,1,0,1,1],[1,1,0,0,1,0,],[0,0,0,1,1,0],[1,0,0,0,0,1],[1,0,0,0,0,0]]
tickets = input('Введите количество билетов: ')
for row in cinema:
    row_str = ''.join(map(str,row))
    if row_str.partition(int(tickets) * '0')[1] != '':
        row_num = cinema.index(row)
        break
else:
    row_num = False
print('Номер ряда: ', row_num)



