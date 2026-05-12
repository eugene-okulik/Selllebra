"""
Напишите программу,
 которая добавляет ‘ing’ в конец слов (к каждому слову)
 в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
 Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
 и после этого выводит получившийся текст на экран.
 Знаки препинания не должны оказаться внутри слова.
 Если после слова идет запятая или точка, этот знак препинания должен идти
 после того же слова, но уже преобразованного.
"""
line = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. \
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
list_from_line = line.split(' ')
print(list_from_line)
modified_list = []
for word in list_from_line:
    if word.endswith(','):
        word = word.rstrip(',')
        modified_list.append(word+'ing'+',')
    elif word.endswith('.'):
        word = word.rstrip('.')
        modified_list.append(word+'ing'+'.')
    else:
        modified_list.append(word+'ing')
result = ' '.join(modified_list)
print(result)

