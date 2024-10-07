print("Дан список чисел: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]")
print("Задача: выбрать из этого списка сначала простые числа, "
      "а затем выбрать составные.")
print("Единица не является ни простым, ни составным числом - "
      "её необходимо исключить.")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
numbers_bez_1 = list(filter(lambda x: x != 1, numbers))
for i in range(len(numbers_bez_1)):
    for j in range(2, numbers_bez_1[i]):
        if (numbers_bez_1[i] % j == 0):
            not_primes.append(numbers_bez_1[i])
        else:
            primes.append(numbers_bez_1[i])
primes = set(numbers_bez_1) - set(not_primes)
print("Простые числа:", list(primes))
print("Составные числа:", list(set(not_primes)))
# Работает с любым количеством чисел в списке и с любым положением единицы в списке.
# Проверяла :-)