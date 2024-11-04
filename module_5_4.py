class House:
    houses_history = []

    def __new__(cls, *args):
        # print(*args)  # проверяла, что распаковывается
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    # def __str__(self):  # проверяла , что принимается в качестве объекта
    #     return f'Название: "{self.name}", количество этажей: {self.number_of_floors}'

    def __del__(self):
        # print(f"Выполняется del c {self.name}") # лишняя проверка, отрабатывает ли метод и с чем
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
# print(h1)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
# print(h2)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
# print(h3)
print(House.houses_history)
del h2
del h3
print(House.houses_history)
del h1
# print(h1, h2, h3) # проверяла, существуют ли объекты (не существуют)
