from pprint import pprint
# Немного усложнила себе задачу. Сначала организовала запись в файл нескольких продуктов,
# далее по заданию - считать данные из файла и через проверку добавить новые продукты через add.
# Однако саму проверку (наличие продуктов в файле) так и не удалось выполнить.
# Как правильно записать проверку?
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

class Shop(Product):
    __file_name = 'products.txt'
    # gp = ''

    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)

    def new_products(self, *products_1):
        file = open(self.__file_name, 'a')
        for item in products_1:
            file.writelines(f"{str(item)}\n")
        file.close()

    def get_products(self):
        file = open(self.__file_name, 'r')
        # gp = str(pprint(file.readlines()))
        pprint(file.read())
        file.close()
        # return gp

    def add(self, *products_2):
        file = open(self.__file_name, 'r+')
        # pprint(file.read())
        for item in products_2:
            if str(item) in str(pprint(file.read())): # Как тут правильно записать?
                print(f"Продукт {str(item)} уже есть в магазине")
            else:
                # file = open(self.__file_name, 'a+')
                file.writelines(f"{str(item)}\n")
        file.close()

        return self.get_products

s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Tomato', 8.2, 'Vegetables')
p5 = Product('Lemon', 2.7, 'Fruits')

print(p2) # __str__
s1.new_products(p2, p3, p4, p5)
s1.add(p1, p2, p3)
print(s1.get_products())