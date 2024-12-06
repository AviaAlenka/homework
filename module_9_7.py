def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        m = 0
        for i in list(range(result)):
            try:
                if result % i == 0:
                    m += 1
            except ZeroDivisionError as exc:
                continue
        if m > 1: # Игнорируем результат деления на единицу
            print("Составное")
        else:
            print("Простое")
        return result
    return wrapper

@is_prime
def sum_three(*digts):
    res = sum(digts)
    return int(res)

result = sum_three(2, 3, 6)
print(result)