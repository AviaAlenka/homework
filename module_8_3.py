class Car:
    def __init__(self, model: "", vin: int, numbers: ""):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        Car.__is_valid_vin(vin, model)
        Car.__is_valid_numbers(numbers, model)

    def __is_valid_vin(vin_number, model):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber (f"Некорректный тип vin номер: "
                                      f"{type(vin_number)}.\n{model} не создан\n")
        if vin_number not in range(1000000, 9999999):
            raise IncorrectVinNumber(f"Неверный диапазон для vin номера.\n"
                                     f"{model} не создан\n")
        else:
            print("Vin номер корректен")
        return True

    def __is_valid_numbers(numbers, model):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers(f"Некорректный тип данных для номеров.\n"
                                      f"{model} не создан\n")
        if len(numbers) != 6:
            raise IncorrectCarNumbers(f"Неверная длина номера.\n{model} не создан\n")
        else:
            print("Госномер корректен")
        return True
class IncorrectVinNumber(BaseException):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(BaseException):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан\n')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан\n')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан\n')