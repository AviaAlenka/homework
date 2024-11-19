from pprint import pprint

class Product:

    # def __new__(cls, *args):
    #     return super().__new__(cls)

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    products = []
    def __str__(self):
        self.products.append(f"{str(self.name)}, {float(self.weight)}, {str(self.category)}")
        return str(self.products)

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        # return f'{pprint(file.read())}'

    def add(self, *products):
        products = Product.products

        file = open(self.__file_name, 'a')
        file.write(f"\n {str(products)}")
        file.close()
        return str(products)

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1, p2, p3) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
print(s1.add())
