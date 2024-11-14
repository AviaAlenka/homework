class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = True



    # def __init__(self, sides, color, filled):
    #     self.__sides = sides
    #     self.__color = color
    #     self.filled = filled

    def get_color(self):
        pass

    def __is_valid_color(self):
        pass

    def set_color(self):
        pass

    def __is_valid_sides(self):
        pass

    def get_sides(self):
        pass

    def __len__(self):
        pass

    def set_sides(self, *new_sides):
        pass


class Circle(Figure):
    sides_count = 1

class Triangle(Figure):
    sides_count = 3

class Cube(Figure):
    sides_count = 12



