num_st = input('Введите 5-тизначное число: ')
print(num_st)
if 5 >= len(str(num_st)) >= 1:
    num_st = int(num_st)

    place_5 = num_st // 10000
    place_4 = num_st // 1000 % 10
    place_3 = num_st // 100 % 10
    place_2 = num_st // 10 % 10
    place_1 = num_st % 10

    print('place_5 = ', place_5)
    print('place_4 = ', place_4)
    print('place_3 = ', place_3)
    print('place_2 = ', place_2)
    print('place_1 = ', place_1)

    num_end = place_5 * 10000 + place_2 * 1000 + place_3 * 100 + place_4 * 10 + place_1
    if place_5 == 0:
        num_end = '0' + str(num_end)
        if place_2 == 0:
            num_end = '0' + str(num_end)
            if place_3 == 0:
                num_end = '0' + str(num_end)
                if place_4 == 0:
                    num_end = '0' + str(num_end)

    print(num_end)
else: print('Введено не 5-тизначное число')