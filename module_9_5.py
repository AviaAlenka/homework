# Вот хоть режьте, не понимаю, как записать в результат итерации элемент start...

class StepValueError(ValueError):
    pass

class  Iterator:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        if self.step == 0:
            raise StepValueError('шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        # self.pointer = self.start - self.step # Да, метод подгона,
                                                # но с такой записью всё работало корректно :-(
        return self

    def __next__(self):
        if self.step > 0 and self.pointer < self.stop:
            self.pointer += self.step
            return self.pointer
        if self.step < 0 and self.pointer > self.stop:
            self.pointer += self.step
            return self.pointer
        raise StopIteration()

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
