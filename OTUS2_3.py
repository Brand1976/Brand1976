st_sequence = 'aaabbbbccccccddddaaaaa'
end_sequence = ''
old_letter = ''
num = 0
for letter in st_sequence:
    if letter == old_letter:
        num += 1
    else:
        if old_letter != '':
            end_sequence += str(num)+old_letter
        num = 1
    old_letter = letter
end_sequence += str(num) + old_letter
print(end_sequence)