n = int(input("Число в первом поле: "))
pole_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
m = int(n/2 +1)
result = []
parol_1 = ()
parol_2 = ()
for i in range(len(pole_2[0:m])):
    k = 1
    while (pole_2[i] + pole_2[i+k]) <= n:
        if n % (pole_2[i] + pole_2[i+k]) == 0:
            parol_1 = pole_2[i]
            parol_2 = pole_2[i+k]
            result.append(parol_1)
            result.append(parol_2)
        k += 1
print("Пароль:")
print("".join(map(str,result)))