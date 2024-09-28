# В качестве словаря возьмём состав чата поиска поискового отряда ЛизаАлерт
print("Состав чата поиска:")
my_dict = {'Тори': "Региональный представитель", 'Шпилька': "Инфорг", 'Оса': "Координатор", 'Чуча': "Старший на месте", 'Гоблин': "Опертивный картограф"}
print(my_dict)
print("Вопрос: какую функцию на поиске выполняет Шпилька, а какую Мася?")
print("Шпилька -", my_dict.get('Шпилька'), "Мася -", my_dict.get('Мася'))
print("Как видим, Маси в чате поиска нет")
print("Добавим Масю в чат и заменим оперативного картографа")
my_dict['Мася'] = "Регистратор"
my_dict['Алёнка'] = "Оперативный картограф"
del my_dict['Гоблин']
print("Обновлённый состав чата:")
print(my_dict)
# В качестве множества возьмём поисковые группы в том порядке, в котором они уходили на задачи
print("В процессе поисковых работ в первый день группы уходили на задачи в такой последовательности:")
print("Кинолог, Лиса, Лиса, Лиса, Ветер, Лиса, БПЛА, Лиса, Ветер, Лиса")
print("Вопрос: какие виды поисковых групп работали на поиске в первый день?")
my_set = {'Кинолог', 'Лиса', 'Лиса', 'Лиса', 'Ветер', 'Лиса', 'БПЛА', 'Лиса', 'Ветер', 'Лиса'}
print(my_set)
print("На следующий день поисковые работы выполнялись автономной группой, а так же работала авиация (Борт)")
print("А кинолог в первый день по каким-то причинам задачу отработать не смог")
print("Всего на поиске было задействовано 35 поисковиков, выполнено 14 задач (10 в первый день и 4 во второй)")
print("Вопрос: какие виды поисковых групп работали на поиске в течение двух дней? Общее число человек и выполненных задач по дням")
my_set.discard('Кинолог')
my_set.add('Автоном')
my_set.add('Борт')
my_set.add(35)
my_set.add((10, 4))
print(my_set)

