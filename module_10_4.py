import queue
import threading
import time
import random
from queue import Queue

class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(threading.Thread):
    def __init__(self, *name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # while not queue.Empty():
        time.sleep(random.randint(3, 10))
        # queue.put(self.name)
        print(f"Новый гость: {self.name}")

class Cafe:
    def __init__(self, queue, *tables):
        self.queue = queue
        self.tables = tables


    def guest_arrival(self, *guests):
        for item in tables:
            # if table.guest is None:
            g = 
            guest = threading.Thread(target=Guest.run, args=(g, ))
            guest.start()
            print(f"{Guest.name} сел(а) за стол номер {item}")

    def discuss_guests(self):
        pass


tables = [Table(number) for number in range(1, 6)]
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra']
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()


Danil Ibatullin
21:53
def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                if table.guest is None:
                    guest.start()
                    table.guest = guest
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
                    https: // t.me / Roman_Urbann