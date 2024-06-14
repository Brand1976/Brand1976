def snake_case(txt):
    string = txt.split('_')
    result = ''
    for word in string:
        result += word.capitalize()
    return result

def camel_case(txt):
    result = txt[0].lower()
    for i in range(1, len(txt)):
        if txt[i].isupper():
            result += '_' + txt[i].lower()
        else:
            result += txt[i]
    return result

text = input('Введите фразу: ')
if text.count('_'):
    result = snake_case(text)
else:
    result = camel_case(text)
print(result)