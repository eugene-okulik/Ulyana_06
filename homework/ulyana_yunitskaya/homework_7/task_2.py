words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for name, number in words.items():
    print(f'{name}' * int(number))
