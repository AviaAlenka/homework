# В функции calculate_average есть непонятный момент. Разъясните, пожалуйста!

def personal_sum(numbers):
    global result
    global correct_data
    global incorrect_data
    result = 0
    correct_data = 0
    incorrect_data = 0
    try:
        for item in numbers:
            try:
                result += item
                correct_data += 1
            except TypeError as exc:
                print(f"Некорректный тип данных: {item}")
                incorrect_data += 1
            continue
    except TypeError as exc:
        print(f"В numbers записан некорректный тип данных (не коллекция): {numbers}")
        incorrect_data += 1
        result = None
    return print(f"Сумма чисел и колчество некорректных данных:"
                 f" {(result, incorrect_data)}"), correct_data


def calculate_average(numbers):
    personal_sum(numbers)
    global correct_data # ВОПРОС: почему для этой переменной нужна эта эта запись,
                        # в для result нет? Они же одинаково определяются и используются...
    try:
        average = result / correct_data
        print(f"Выполняется Try в calculate_average с {numbers}:"
              f" {result}/{correct_data}: {average}")
        return average
    except ZeroDivisionError as exc:
        correct_data = 0
        print(f"Исправляется ZeroDivisionError: {correct_data}")
        return correct_data
    except TypeError as exc:
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}\n') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}\n') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}\n') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать