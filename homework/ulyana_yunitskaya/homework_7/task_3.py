txt_1 = 'результат операции: 42'
txt_2 = 'результат операции: 54'
txt_3 = 'результат работы программы: 209'
txt_4 = 'результат: 2'


def process_line(line):
    full_text = line[:line.index(':')]
    number = int(line.split(':')[-1].strip())
    return full_text, number + 10


for txt in [txt_1, txt_2, txt_3, txt_4]:
    label, result = process_line(txt)
    print(f"{label}: {result}")
