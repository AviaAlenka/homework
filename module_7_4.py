team1 = "Мастера Кода"
team2 = "Волшебники Данных"
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

print("Используем %:")
print('В команде "%s" участников - %s' % (team1, team1_num))
print('В команде "%s" участников - %s' % (team2, team2_num))
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print("\nИспользуем format():")
print('Команда "{}" решила задач: {}'.format(team1, score_1))
print('"{}" решили задачи за {}c'.format(team1, team1_time))
print('Команда "{}" решила задач: {}'.format(team2, score_2))
print('"{}" решили задачи за {}c'.format(team2, team2_time))
print("\nИспользуем f-строки:")
print(f'Команды решили {score_1} и {score_2} задач')
print("Итоги соревнований:")
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print(f'Победа команды "{team1}"!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды "{team2}"!')
else:
    print('Ничья!')
print(f'Сегодня было решено {tasks_total} задачи, в среднем по {time_avg} секунды на задачу!')
