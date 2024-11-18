import math

class Figure:
    sides_count = 0
    filled = True

    def __init__(self, txt, color, *sides):
        self.__sides = sides
        self.__color = color

    # def __is_valid_color(self, r, g, b): # Почему-то не срабатывает...
    #     if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
    #         return True

    def set_color(self, r, g, b):
        print(f"Получены новые цвета в {self.__class__.__name__}: {r}, {g}, {b}")
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
        # if self.__is_valid_color is True: # Не срабатывает, перебрасывает на Else...
            print(f"Новые цвета {self.__class__.__name__}: {r}, {g}, {b}")
            self.__color = (r, g, b)
        else:
            print(f"Недопустимый цвет {self.__class__.__name__}. "
                  f"Цвета остались старыми: {self.__color}")
        return self.__color

    def get_color(self):
        print(f"Цвета {self.__class__.__name__}: {self.__color}")
        return self.__color

    def __is_valid_sides(self):
        # После неудачного опыта с __is_valid_color не понимаю, как выполнить
        pass

    def get_sides(self):
        print(f"Исходные стороны в {self.__class__.__name__}: {list(self.__sides)}")
        if len(self.__sides) == 1:
            a = self.__sides[0]
            list_of_a = [a] * self.sides_count
            print(f"Стороны в {self.__class__.__name__}: {list_of_a}")
            self.__sides = list_of_a
        elif len(self.__sides) != self.sides_count:
            a = 1
            list_of_a = [a] * self.sides_count
            print(f"Новые стороны в {self.__class__.__name__}:{list_of_a}")
            self.__sides = list_of_a
        return self.__sides

    def set_sides(self, *new_sides):
        self.new_sides = list(new_sides)
        print(f"Получены новые стороны в {self.__class__.__name__}:{self.new_sides}")

        if len(self.new_sides) == 1:
            a = self.new_sides[0]
            list_of_a = [a] * self.sides_count
            print(f"Новые стороны в {self.__class__.__name__}: {list_of_a}")
            self.new_sides = list_of_a
            return self.new_sides
        elif len(self.new_sides) != self.sides_count:
            print(f"Неверные стороны {self.__class__.__name__}")
            self.new_sides = self.__sides
            return self.new_sides

    def __len__(self):
        # len = self.__sides * self.sides_count
        print(f"Периметр фигуры {self.__class__.__name__}: {sum(self.new_sides)}")
        return sum(self.new_sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, sides)

    print(f"Количество сторон у круга: {sides_count}")

    def get_square(self):
        square = (self.new_sides[0] ** 2) / (4 * math.pi)
        __radius = self.new_sides[0] / (2 * math.pi) # Вне метода не удалось записать
        print(f"Радиус круга: {__radius}")
        print(f"Площадь круга: {square}")

        return square

class Triangle(Figure):
    sides_count = 3
    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, *sides)
    print(f"Количество сторон у треугольника: {sides_count}")

    def get_square(self):
        A =  self.new_sides[0]
        square = (A**2*math.sqrt(3))/4
        print(f"Площадь треугольника: {square}")
        return square

class Cube(Figure):
    sides_count = 12
    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, *sides)
    print(f"Количество рёбер у квадрата: {sides_count}")

    def get_volume(self):
        volume = self.new_sides[0] ** 3
        print(f"Объём куба: {volume}")
        return volume

circle1 = Circle("Круг", (200, 200, 100), 10)
circle1.set_color(255, 66, 77)
print(circle1.get_color())
circle1.get_sides()
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

triangle1 = Triangle("Треугольник", (50, 50, 50), 10, 6)
triangle1.set_color(11, 255, 344)
print(triangle1.get_color())
triangle1.get_sides()
triangle1.set_sides(7)
print(triangle1.get_sides())

cube1 = Cube("Куб", (222, 35, 130), 6)
cube1.set_color(63, 98, 244)
print(cube1.get_color())
cube1.get_sides()
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
print(len(circle1))
print(len(triangle1))
print(len(cube1))
print(circle1.get_square())
print(triangle1.get_square())
print(cube1.get_volume())