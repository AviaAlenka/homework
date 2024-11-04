class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: "{self.name}", количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        print(f"Сравниваются {self.number_of_floors} и {other.number_of_floors}")
        return self.number_of_floors == other.number_of_floors
    # def __lt__(self, other):
    #     return self.number_of_floors < other.number_of_floors
    # def __le__(self, other):
    #     return self.number_of_floors <= other.number_of_floors
    # def __gt__(self, other):
    #     return self.number_of_floors > other.number_of_floors
    # def __ge__(self, other):
    #     return self.number_of_floors >= other.number_of_floors
    # def __ne__(self, other):
    #     return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        print(f"В '{self.name}' будет добавлено {value} этажей")
        # self.number_of_floors + value
    #     # if isinstance(value, House):
    #     #     return House(self.number_of_floors + value.number_of_floors)
    #     # else:
        return self
        # return f'Название: "{self.name}", количество этажей: {self.number_of_floors + value}'
    def  __radd__(self, value):
        return self #.__add__(value)
    def __iadd__(self, value):
        print(f"В '{self.name}' будет добавлено {value} этажей")
        self.number_of_floors += value
        # return f'Название: "{self.name}", количество этажей: {self.number_of_floors + value}'
        return self


    #
    #     self.number_of_floors += value.number_of_floors
    #     # print(f"В '{self.name}' будет добавлено {value} этажей")
    #     return f'Название: "{self.name}", количество этажей: {self.number_of_floors + value}'

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(f"Выполняется h1 == h2: {h1 == h2}")
h1 = h1 + 25
h2 = h2 + 15
print(h1)
print(h2)
print(f"Выполняется h1 == h2: {h1 == h2}")
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
# print(h1 < h2)
# print(h1 <= h2)
# print(h1 > h2)
# print(h1 >= h2)
# print(h1 != h2)

