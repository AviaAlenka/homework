# Сделеле в двух вариантах - с ручным вводом строк и по заданию

def add_everything_up_2(a, b):
    a = input("Введите первую строку: ")
    b = input("Введите вторую строку: ")
    # print(type(a), type(b)) # str
    try:
        c = [float(a), float(b)]
        print(sum(c))
    except ValueError as exc:
        print(f"Исправляется ValueError: {a + b}")

def add_everything_up(m, n):
    # print(type(m))
    # print(type(n))
    try:
        s = m + n
        return round(s, 4)
    except TypeError as exc:
        return (f"Исправляется TypeError: {str(m) + str(n)}")

print("Давайте будем складывать строки!")
a = float
b = float
add_everything_up_2(a, b)

print("\nТеперь строго по заданию.\nНеобходимо сложить строки:\n"
      "123.456 и 'строка'\n'яблоко' и 4215\n123.456 и 7\n")
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

