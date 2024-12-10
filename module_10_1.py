import threading
import datetime
from time import sleep
import time
def write_words(word_count, file_name = ''):
    file = open(file_name, 'a', encoding='utf-8')
    for item in range(1, word_count + 1):
        file.writelines(f"Какое-то слово № {item}\n")
        time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
    file.close()

start = datetime.datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
finish = datetime.datetime.now()
elapsed_time = finish - start
print(f"Работа потоков {str(elapsed_time)}")

start2 = datetime.datetime.now()
thread = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread.start()
thread = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread.start()
thread2 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread2.start()
thread = threading.Thread(target=write_words, args=(100, "example8.txt"))
thread.start()
thread2.join()
finish2 = datetime.datetime.now()
elapsed_time2 = finish2 - start2
print(f"Работа потоков {str(elapsed_time2)}")