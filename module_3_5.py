number = int(input("Введите число: "))
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    print(first) # проверка, какие цифры берутся для расчётов
    if len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))

print("Произведение цифр этого числа:", get_multiplied_digits(number))

