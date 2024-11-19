from pprint import pprint

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

    def __init__(self, name, weight, category):
        super().__init__(name, weight, category)

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        # return self.get_products


    def add(self, *products):
        file = open(self.__file_name, 'a')
        for item in products:
            # if self is str(item) or self == str(item):
            if item in products:
                print(f"{str(item)} уже есть в магазине")
            else:
                file.writelines(f"{str(item)}\n")

        file.close()
        return self.get_products

s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())

