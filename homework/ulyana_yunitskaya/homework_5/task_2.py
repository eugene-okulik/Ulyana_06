txt = 'результат операции: 52'
colon_index = txt.index(':')
label = txt[:colon_index]
user_input = int(txt[colon_index + 1:]) + 10
print(f'{label}: {user_input}')

text = 'результат операции: 514'
find_index = text.index(':')
new = text[:find_index]
user_input_1 = int(text[find_index + 1:]) + 10
print(f'{new}: {user_input_1}')


text_2 = 'результат работы программы: 9'
find_index_2 = text_2.index(':')
new_2 = text_2[:find_index_2]
user_input_2 = int(text_2[find_index_2 + 1:]) + 10
print(f'{new_2}: {user_input_2}')
