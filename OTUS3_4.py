def check_user(user_):
    name, surname, age, id = user_.split(',')
    if name.isalpha() or surname.isalpha():
        name = name.strip().capitalize()
        surname = surname.strip().capitalize()
    else:
        print('Имя или Фамилия введены не корректно, введите заново')
        return
    if not age.strip().isdigit() or not 18 <= int(age.strip()) <= 60:
        print('Возраст введен не корректно, введите заново')
        return
    if id.strip().isdigit() and 1 <= int(id.strip()) <= 99999999:
        len_ID = len(id.strip())
        id = (8-len_ID)*'0' + id.strip()
    else:
        print('ID введен не корректно, введите заново')
        return
    return name, surname, age.strip(), id

users = {}
while True:
    user = input('Введите через запятую Имя,Фамилию,Возраст и ID пользователя: ')
    if user == '':
        print('Ввод пользователей закончен')
        break
    user = check_user(user)
    if not user:
        continue
    if user[3] in users:
        print('Такой ID уже есть в списке, введите заново')
        continue
    else:
        users[user[3]] = [user[0], user[1], user[2]]
    print(users)

print('| %-8s | %-20s | %-20s | %-7s |' % ('ID', 'Имя', 'Фамилия', 'Возраст'))
for user in users.items():
    print('| %-8s | %-20s | %-20s | %-7s |' % (user[0], user[1][0], user[1][1], user[1][2]))
