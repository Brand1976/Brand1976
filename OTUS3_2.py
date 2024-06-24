def check_data(day, month, year):
    #print(day, month, year)
    if 1 <= month <= 12 and 1 <= day <= 31:
        if month == 1 and day <= 31:
            return True
        elif month == 2 and day <= 28:
            return True
        elif month == 2 and (not year % 4 and year % 100 or not year % 400) and day <= 29:
            return True
        elif month == 3 and day <= 31:
            return True
        elif month == 4 and day <= 30:
            return True
        elif month == 5 and day <= 31:
            return True
        elif month == 6 and day <= 30:
            return True
        elif month == 7 and day <= 31:
            return True
        elif month == 8 and day <= 31:
            return True
        elif month == 9 and day <= 30:
            return True
        elif month == 10 and day <= 31:
            return True
        elif month == 11 and day <= 30:
            return True
        elif month == 12 and day <= 31:
            return True
        else:
            return False
    else:
        return False


#date = input('Введите дату в формате ДД.ММ.ГГГГ: ')
date = ('29.02.2000')
day, month, year = map(int, date.split('.'))
print(check_data(day, month, year))
