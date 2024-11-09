class Animal:
    alive = True
    fed = False
    # name = []
    # def __new__(cls, name): # пробовала добавить. Что с ним, что без него - результат одинаковый
    #     cls.name.append([0])
    #     return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if Plant.edible is True: # Если True поменять на False, все всё съедают, живы и сыты
            fed = True
            # print(fed, alive) # проверяю обновлённые атрибуты.
            #                     # alive из родительского класса не видит, ошибка
            Animal.fed = True
            print(Animal.fed, Animal.alive)
            print(f"{self.name} съел {food.name}")
            # return fed
        else:
            # alive = False
            Animal.alive = False
            print(Animal.fed, Animal.alive)
            print(f"{self.name} не стал есть {food.name}")

class Mammal(Animal):
    # def eat(self, food): # - перенесла в родительский класс
    #     if Plant.edible is True:
    #         Animal.fed = True # - пробовала и fed = True
    #         print(f"{self.name} съел {food.name}")
    #         # return fed
    #     else:
    #         Animal.alive = False # - пробовала и alive = False
    #         print(f"{self.name} не стал есть {food.name}")
    pass
class Predator(Animal):
    # def eat(self, food): # - перенесла в родительский класс
    #     if Plant.edible is True:
    #         Animal.fed = True
    #         print(f"[{self.name} съел {food.name}")
    #
    #     else:
    #         Animal.alive = False
    #         print(f"{self.name} не стал есть {food.name}")
    pass

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name

class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(f"{p1.name} съедобен - {p1.edible}") # - проверяю атрибуты объектов класса
print(f"{p2.name} съедобен - {p2.edible}") # - проверяю атрибуты объектов класса
print(a1.name)
print(p1.name)

print(f"{a1.name} жив - {a1.alive}")
print(f"{a2.name} сыт - {a2.fed}")
a1.eat(p1)
print(f"{a1.name} жив - {a1.alive}")
print(f"{a1.name} сыт - {a1.fed}")

a2.eat(p2)
print(f"{a2.name} жив - {a2.alive}")
print(f"{a2.name} сыт - {a2.fed}")

print(a1.alive)
print(a2.fed)

# При первоначальной проверке атрибутов еды всё работает корректно.
# При выполнении команд a1.eat(p1) и a2.eat(p2) условие из eat(self, food) видит только
# атрибут еды из родительского класса class Plant. Переназначенные атрибуты в дочерних
# классах не видит. Что я делаю не так?
