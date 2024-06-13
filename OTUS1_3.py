length = int(input('Введите длинну шоколада в кусочках: '))
width = int(input('Введите ширену шоколада в кусочках: '))
piece = int(input('Введите сколько кусков Вы хотите получить за один разлом: '))
if piece % length == 0 and piece/length < width: print('ДА')
elif piece % width == 0 and piece/width < length: print('ДА')
else: print('НЕТ')

