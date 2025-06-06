my_dict = {
    'tuple': (23, 18, 5.45, 'cat', True),
    'list': [13, None, 'door', 2.65, False],
    'dict_new': {
        'car': 'sheep',
        'car1': 'sheep1',
        'car2': 'sheep2',
        'car3': 'sheep3',
        'car4': 'sheep4'
    },
    'set': {12, 33, 'dog', 13.12, 'frog'}
}

print(my_dict['tuple'][-1])

my_dict['list'].append(18)
# print(my_dict['list'])
my_dict['list'].pop(1)
# print(my_dict['list'])

my_dict['dict_new']['i am a tuple'] = 'crazy'
# print(my_dict['dict_new'])

my_dict['dict_new'].pop('car1')
# print(my_dict['dict_new'])

my_dict['set'].add(876)
# print(my_dict['set'])

my_dict['set'].pop()
# print(my_dict['set'])

print(my_dict)
