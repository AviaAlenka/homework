immutable_var = "Маленькая кучка данных:", 1, True, "и", 2.5, False
print(immutable_var)
# immutable_var [0] = "Большая кучка данных:" - попытка изменить первый элемент
print(immutable_var)
print("Не удалось изменить первый элемент в перечне данных, поскольку перечень задан кортежем, а не списком")
print("Перелаем перечень в тип 'список':")
mutable_list = ["Маленькая кучка данных:", 1, True, "и", 2.5, False]
print(mutable_list)
print("Попробуем изменить первый элемент списка и добавить элементов в список:")
mutable_list = ["Маленькая кучка данных:", 1, True, "и", 2.5, False, "35*6", 10**2, type(5.2)]
mutable_list [0] = "Большая кучка данных:"
print(mutable_list)
print("Получилось!")