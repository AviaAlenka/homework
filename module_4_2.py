def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # Вызывается только отсюда, из локальной области функции test_function, причём
                     # только в паре с вызовом самой функции test_function из глобального пространства имён
test_function()
# inner_function() - Отсюда не вызывается. Ошибка: "Функция inner_function не определена"