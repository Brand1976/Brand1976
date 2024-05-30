alphabet = 'abcdefghijklmnopqrstuvwxyz'
start_text = 'Hello Stone'
key = 3
end_text = ''

for letter in start_text:
    if letter == ' ':
        end_text += ' '
    elif letter.isupper():
        letter = letter.lower()
        i = alphabet.find(letter)
        if i + key > 25:
            i2 = i + key - 26
        else: i2 = i + key
        end_text += alphabet[i2].upper()
    else:
        i = alphabet.find(letter)
        if i + key > 25:
            i2 = i +key - 26
        else: i2 = i + key
        end_text += alphabet[i2]
print(end_text)
