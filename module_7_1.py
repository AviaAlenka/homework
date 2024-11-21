from pprint import pprint
# Немного усложнила себе задачу. Сначала организовала запись в файл нескольких продуктов,
# далее по заданию - считать данные из файла и через проверку добавить новые продукты через add.

class Product:

    def __new__(cls, *args):
        return super().__new__(cls)

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    product = ""
    def __str__(self):
        self.product = f"{str(self.name)}, {float(self.weight)}, {str(self.category)}"
        return str(self.product)

class Shop:
    __file_name = 'products.txt'
    gp = []

    # def new_products(self, *products_1): # Если раскомментировать, тоже работает :-)
    #     file = open(self.__file_name, 'a')
    #     for item in products_1:
    #         file.writelines(f"{str(item)}\n")
    #     file.close()
    #     file = open(self.__file_name, 'r')
    #     pprint(file.readlines())
    #     file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        self.gp = file.readlines()
        file.close()
        # print(f"Строка для проверки 1: {self.gp}")
        return self.gp

    def add(self, *products_2):
        file = open(self.__file_name, 'a')
        # print(f"Строка для проверки 2: {self.get_products()}")
        for item in products_2:
            if str(item) in str(self.get_products()):
                print(f"Продукт {str(item)} уже есть в магазине")
            else:
                file.writelines(f"{str(item)}\n")
                print(f"Продукт {str(item)} добавлен в магазин")
        file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Tomato', 8.2, 'Vegetables')
p5 = Product('Lemon', 2.7, 'Fruits')

print(p2) # __str__
# s1.new_products(p2, p3, p4, p5) # Можно раскомментировать вместе с new_products()
s1.add(p1, p2, p3)
print(f"В магазине теперь:\n{'\n'.join(s1.get_products())}")