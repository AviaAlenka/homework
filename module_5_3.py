class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: "{self.name}", количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        print(f"Сравниваются {self.number_of_floors} и {other.number_of_floors}") # для проверки, что принимается к сравнению
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __add__(self, value):
        print(f"В '{self.name}' будет добавлено {value} этажей") # для проверки, что и куда принимается
        self.number_of_floors += value
        return self
    def  __radd__(self, value):
        print(f"В '{self.name}' будет добавлено {value} этажей")
        self.number_of_floors += value
        return self #.__add__(value)
    def __iadd__(self, value):
        print(f"В '{self.name}' будет добавлено {value} этажей")
        self.number_of_floors += value
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(f"Выполняется h1 == h2: {h1 == h2}")
h1 = h1 + 10
# h2 = h2 + 15 # проверяла работоспособность
print(h1)
print(h2)
print(f"Выполняется h1 == h2: {h1 == h2}")
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
