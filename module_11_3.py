# Для выполнения задания взяла свою же домашнюю работу module_6_2
import inspect
from pprint import pprint


class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = int(__engine_power)

    def get_model(self):
        print(f"Модель: {self.__model}")
    def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power} л.с.")
    def get_color(self):
        print(f"Цвет: {self.__color}")
    def get_owner(self):
        print(f"Владелец: {self.owner}")
    def print_info(self):
        return self.get_model(), self.get_horsepower(), self.get_color(), self.get_owner()
    def set_color(self, other):
        new_color = other
        if new_color.lower() in str(self.__COLOR_VARIANTS).lower():
            self.__color = new_color
            return self.__color
        else:
            print(f"Нельзя сменить цвет на {new_color}")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500.5)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()

def introspection_info(obj):
    # help(obj) # для посмотреть
    print(f"Тип объекта: {type(obj)}")
    # pprint(dir(obj)) # тоже для посмотреть
    a = dir(obj)
    attr = list(filter(lambda a: a[0] == "_" and a[1] != "_", a))
    print(f"Атрибуты: {attr}")
    methods = list(filter(lambda a: a[0:2] == "__" or a[0] != "_", a))
    print(f"Методы: {methods}")
    print(inspect.getmodule(obj))

# obj = Vehicle # проверяла с разными классами
obj = Sedan
introspection_info(obj)