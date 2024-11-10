import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, _cords, speed):
        self._cords = _cords
        self.speed = speed

    _cords = [0, 0, 0]
    speed = int()

    def move(self, dx, dy, dz):
        pass

    def get_cords(self):
        pass

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER > 5:
            print("Be careful, i'm attacking you 0_0")

    def about(self):
        print("Ку-ку")

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
        pass

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal, Animal):
    sound = "Click-click-click"
    def __init__(self, _cords, speed):
        super().__init__(_cords, speed)
        super().about()
    def speak(self):
        print(self.sound)

    

db = Duckbill(10, 10)

print(f"Животное живо: {db.live}")
print(f"У животного есть клюв: {db.beak}")

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()