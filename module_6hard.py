import math

class Figure:
    sides_count = 0
    filled = True

    def __init__(self, txt, color, *sides):
        self.__sides = sides
        self.__color = color

    def set_color(self, r, g, b):
        print(f"Получены новые цвета в {self.__class__.__name__}: {r}, {g}, {b}")
        if r in range(0, 256) and g in range(0, 256) and b in range(0, 256):
            print(f"Новые цвета {self.__class__.__name__}: {r}, {g}, {b}")
            self.__color = (r, g, b)
        else:
            print(f"Недопустимый цвет {self.__class__.__name__}. "
                  f"Цвета остались старыми: {self.__color}")
        return self.__color

    def get_color(self):
        # __color = []
        print(f"Цвета {self.__class__.__name__}: {self.__color}")
        return self.__color

    def __is_valid_sides(self):
        pass


    def set_sides(self, *new_sides):
        self.__sides = list(new_sides)
        print(f"Получены новые стороны в {self.__class__.__name__}:{self.__sides}")
        if len(self.__sides) == 1:
            a = self.__sides[0]
            list_of_a = [a] * self.sides_count
            print(f"Новые стороны в {self.__class__.__name__}: {list_of_a}")
            self.__sides = list_of_a
            # return self.__sides
        else:
            # a = 1
            # list_of_a = [a] * self.sides_count
            # print(f"Новые стороны в {self.__class__.__name__}:{list_of_a}")
            # self.__sides = list_of_a
            print(f"Cтороны в {self.__class__.__name__} остались старыми:{self.__sides}")
            # self.__sides = list_of_a

    def get_sides(self):
        print(f"Исходные стороны {self.__class__.__name__}: {list(self.__sides)}")
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

    def __len__(self):
        # len = self.__sides * self.sides_count
        print(f"Периметр фигуры {self.__class__.__name__}: {sum(self.__sides)}")
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, sides)

    print(f"Количество сторон у круга: {sides_count}")

    # __radius = sides / (2 * math.pi)
    # print(f"Радиус круга: {__radius}")

class Triangle(Figure):
    sides_count = 3
    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, *sides)
    print(f"Количество сторон у треугольника: {sides_count}")

class Cube(Figure):
    sides_count = 12
    def __init__(self, txt, color, *sides):
        super().__init__(txt, color, *sides)
    print(f"Количество рёбер у квадрата: {sides_count}")

    def get_volume(self):
        volume = self.__sides[0] ** 3
        print(f"Объём куба: {volume}")

circle1 = Circle("Круг", (200, 200, 100), 10)
circle1.set_color(255, 66, 277)
print(circle1.get_color())
circle1.get_sides()
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

triangle1 = Triangle("Треугольник", (200, 200, 100), 10, 6)
triangle1.set_color(11, 255, 44)
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