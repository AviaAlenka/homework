from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        # print(f"Товар: {str(self.name)}, {float(self.weight)}, {str(self.category)}")
        return f"{str(self.name)}, {float(self.weight)}, {str(self.category)}"

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return str(file)

    def add(self, *products):
        file = open(self.__file_name, 'a')
        file.writelines(f"\n {products}")
        file.close()
        return str(file)



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p1, p2, p3) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())