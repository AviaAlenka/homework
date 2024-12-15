import datetime
from multiprocessing import Pool

def read_info(name = ""):
    all_data = []
    file = open(name, 'r')
    all_data = file.readlines()
    file.close()
    print(f"Файл {name} прочитан")

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# finish = datetime.datetime.now()
# elapsed_time = finish - start
# print(f"Время линейного выполнения {str(elapsed_time)}")

if __name__ == '__main__':
    start = datetime.datetime.now()
    with Pool(4) as p:
        p.map(read_info, filenames)
    finish = datetime.datetime.now()
    elapsed_time = finish - start
    print(f"Время многопроцессного выполнения {str(elapsed_time)}")