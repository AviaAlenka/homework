import threading
import time
import random

counter = 1
lock = threading.Lock()

class Bank(threading.Thread):
    def __init__(self, balance):
        threading.Thread.__init__(self)
        self.balance = balance

    def deposit(self):
        global counter
        lock.acquire()
        for i in range(100):
            bal = random.randint(50, 500)
            time.sleep(0.001)
            self.balance += bal
            print(f"Пополнение: {bal}. Баланс: {self.balance}")
            if self.balance >= 500 and lock.locked() == True:
                lock.release()
            counter += 1
        return self.balance

    def take(self):
        global counter
        lock.release()
        for i in range(100):
            bal = random.randint(50, 500)
            time.sleep(0.001)
            print(f"Запрос на: {bal}")
            if bal <= self.balance:
                self.balance -= bal
                print(f"Снятие: {bal}. Текущий баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                lock.acquire()
            counter += 1
        return self.balance

bk = Bank(0)
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')