numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k = 0
for i in range(len(numbers)):
    for j in range(2, numbers[i]):
        if (numbers[i] % j == 0):
            k = k+1
    if (k <= 0):
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print(primes)
print(not_primes)

