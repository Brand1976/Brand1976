days = int(input('Введите сколько дней осталось до отпуска: '))
weeks = days//7
plus_days = days - weeks*7
#print(weeks)
#print(plus_days)
if plus_days == 6: weekends = weeks*2 + 1
else: weekends = weeks*2
print('До отпуска осталось ' + str(weekends) + ' выходных')