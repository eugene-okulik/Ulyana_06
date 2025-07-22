import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')
print(eugene_file)


def date_split(line):
    left, instruction = line.split(" - ", maxsplit=1)
    number, date_str = left.split(" ", maxsplit=1)
    return number, date_str, instruction


with open(eugene_file, encoding='utf-8') as eugene_file_1:
    for line in eugene_file_1:
        number, date_str, instruction = date_split(line)
        dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f")
        if "на неделю позже" in instruction:
            result = dt + datetime.timedelta(weeks=1)
        elif "день недели" in instruction:
            result = dt.strftime('%A')
        elif "дней назад" in instruction:
            result = f"{(datetime.datetime.now() - dt).days} дней назад"

        print(f"{number} {result}")
