print("Исходные данные:")
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print("Перечни оценок для учеников в алфавитном порядке:", grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print("Перечень учеников:", students)
print("Задача: вычислить средний балл каждого ученика")
# Перечень учеников дан множеством, не отсортирован по алфавиту, к тому же невозможно обратиться к отдельному его элементу. Поэтому преобразуем это множество в список
# Перечень оценок задан списком, оставим его как есть.
students_list = list(students)
# И отсортируем полученный список
students_list_sort = sorted(students_list)
print("Список учеников в алфавитном порядке:", students_list_sort)
# Для проверки составим словарь из имён учеников и перечней их оценок
zhurnal = {students_list_sort[0]: grades[0],students_list_sort[1]: grades[1],
           students_list_sort[2]: grades[2],students_list_sort[3]: grades[3],
           students_list_sort[4]: grades[4]}
print("Теперь этот список с оценками:")
print(zhurnal)
print("Упорядочили наконец исходные данные :-)")
print("Теперь посчитаем для каждого ученика средний балл.")
grades_med = [sum(grades[0]) / len(grades[0]), sum(grades[1]) / len(grades[1]),
              sum(grades[2]) / len(grades[2]), sum(grades[3]) / len(grades[3]),
              sum(grades[4]) / len(grades[4])]
print("Получаем:")
zhurnal_med = {students_list_sort[0]: grades_med[0],students_list_sort[1]: grades_med[1],
           students_list_sort[2]: grades_med[2],students_list_sort[3]: grades_med[3],
           students_list_sort[4]: grades_med[4]}
print(zhurnal_med)
