import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f"{self.name}, на нас напали!")
        vrag = 100
        days = 0
        while vrag > 0:
            time.sleep(1)
            days += 1
            vrag -= self.power
            print(f"{self.name} сражается {days} дней(дня), осталось {vrag} воинов")
        print(f"{self.name} одержал победу спустя {days} дней(дня)!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
time.sleep(1)
second_knight.start()
first_knight.join()
second_knight.join()

print("Все битвы закончились!")