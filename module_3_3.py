def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print("Дана функция с аргументами по умолчанию: (a = 1, b = 'строка', c = True):")
print("Вызов функции с одним аргументом (а):")
print_params(a=3)
print("Вызов функции с двумя аргументами (а, c):")
print_params(a=638, c=75)
print("Вызов функции с тремя аргументами (а, b, с):")
print_params(a=6, b=False, c="test")
print("Вызов функции без аргументов:")
print_params()
print("Вызов функции с аргументом b = 25:")
print_params(b = 25)
print("Вызов функции с аргументом c = [1,2,3]:")
print_params(c = [1,2,3])

values_list = ["Stroka", False, 98]
values_dict = {'a':67, 'b':35, 'c':133}
print("Передача функции списка ['Stroka', False, 98] с распаковкой:")
print_params(*values_list)
print("Передача функции словаря {'a':67, 'b':35, 'c':133} с распаковкой:")
print_params(**values_dict)
print("Проверка, работает ли print_params(*values_list_2, 42), "
      "где values_list_2 - список с двумя элементами:")
values_list_2 = [54.32, 'Строка' ]

print_params(*values_list_2, 42)
print("Поменяем параметры местами:")
print_params(42, *values_list_2)