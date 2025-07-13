PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

result = {
    key: int(value.replace('р', '')) for key, value in (line.split() for line in PRICE_LIST.split('\n'))
}
print(result)


names = [line.split()[0] for line in PRICE_LIST.split('\n')]
prices = [int(line.split()[1].replace('р', '')) for line in PRICE_LIST.split('\n')]
result_2 = dict(zip(names, prices))
print(result_2)
