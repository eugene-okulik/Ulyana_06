temperatures = [
    20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
    27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23
]

new_form_2 = list(filter(lambda x: x > 28, temperatures))

print(list(new_form_2))
print(max(new_form_2))
print(min(new_form_2))
print(round(sum(new_form_2) / len(new_form_2), 2))
