class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self):
        new_floor = int(input(f"На какой этаж в '{self.name}' необходимо приехать? "))
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(new_floor):
                print(i+1)
        if new_floor <= 2:
            print("Можно и пешком!")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(f"В доме '{h1.name}' {h1.number_of_floors} этажей")
print(f"В доме '{h2.name}' {h2.number_of_floors} этажа")

h1.go_to()
h2.go_to()
