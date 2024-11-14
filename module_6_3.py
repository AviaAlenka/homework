import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed=0):
        self._cords = _cords
        self.speed = speed

    _cords = [0, 0, 0]
    speed = int()

    def move(self, dx, dy, dz):
        if dz < 0:
            print("It's too deep, i can't dive :(")
            # print(Animal._cords) # проверка координат
        else:
            Animal._cords = [(x + y) for x, y in zip(Animal._cords, (dx, dy, dz))]

    def get_cords(self):
        speed = int(Animal.speed) + int(db.speed)
        Animal._cords = (Animal._cords[0] * speed, Animal._cords[1] * speed, Animal._cords[2] * speed)
        # print(Animal._cords)
        print(f"X: {Animal._cords[0]} Y: {Animal._cords[1]}, Z: {Animal._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):
    beak = True

    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)

    def lay_eggs(self):
        random_number = random.randint(1, 4)
        print(f"Here are(is) {random_number} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)

    def dive_in(self, dz):
        # print(f"Класс водоплавающие: {Animal._cords}") # проверка координат
        print(f"X: {Animal._cords[0]} Y: {Animal._cords[1]}, "
              f"Z: {int((Animal._cords[2]  - (abs(dz) * db.speed) / 2))}")

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)

class Duckbill(PoisonousAnimal,Bird, AquaticAnimal,  Animal):
    sound = "Click-click-click"
    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)
    def speak(self):
        print(f"Животное издаёт звуки: {self.sound}")

db = Duckbill(0, 10)
print(f"Животное живо: {db.live}")
print(f"У животного есть клюв: {db.beak}")
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.lay_eggs()
# print(Duckbill.mro()) # проверка порядка наследования