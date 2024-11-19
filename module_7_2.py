# Так и не поняла, как получить байт начала строки, куда ещё надо засунуть tell()...
# И не удалось избавиться от квадратных скобок в словаре...
# Что я делаю не так?

def custom_write(file_name = '', strings = ()):
    file = open(file_name, 'a', encoding='utf-8')
    for item in strings:
        file.writelines(f"{str(item)}\n")
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    strings_positions = {}
    n = 1
    while True:
        line = str(file.readline())
        key, *value = (n, file.tell()), str(line).replace('\n', '')
        strings_positions[key] = value
        n += 1
        if not line:
            break
    file.close()
    # print(strings_positions) # Проверка словаря
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)