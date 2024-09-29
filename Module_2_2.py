print("Сравниваем целые числа")
first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third:
    print("Вы ввели три одинаковых числа")
elif first == second or first == third or second == third:
    print("Вы ввели два одинаковых числа")
else:
    print("Среди введённых Вами чисел нет одинаковых")
