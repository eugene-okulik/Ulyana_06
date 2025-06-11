long_text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. '
             'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero')
words = long_text.split(' ')
word = type(str)

for word in words:
    if '.' in word:
        print(word.replace('.', 'ing.'), end=' ')
    elif ',' in word:
        print(word.replace(',', 'ing,'), end=' ')
    else:
        print(word + 'ing', end=' ')