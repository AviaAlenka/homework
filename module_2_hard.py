n = int(input("Число в первом поле: "))

# pole_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pole_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# index = pole_2.index(n)
m = int((n+0.3)/2)
result = []
parol = ()
parol_2 = ()

# while int(pole_2[j]) < n:
# for j in pole_2[0:m]:
for j in range(m):
    k = 1
    while (pole_2[j] + pole_2[j+k]) <= n:
        if n % (pole_2[j] + pole_2[j+k]) == 0:
            parol_2 = (pole_2[j+k])
            parol = (pole_2[j], parol_2)

        k += 1
        result.append(parol)


    # def result(result_schet):
    #     unique = []
    #     for number in result_schet:
    #         if number in unique:
    #             continue
    #         else:
    #             unique.append(number)
    #     return unique

# for j in range(1,m):
#     k = 1
#     while (j + (j + k)) <= n:
#         if n % (j + (j + k)) == 0:
#             parol_2 = (j+k)
#             parol = (j, parol_2)
#
#         k += 1
#         result.append(parol)


print(n, "-", str(result))


# for i in range(len(pole_1)):
#     k = 1
#     while int(pole_2[j]) < int(pole_1[i]):
#         while (int(pole_2[j]) +int(pole_2[j+k])) <= int(pole_2[j]):
#             if int(pole_1[i]) % (int(pole_2[j]) +int(pole_2[j+k])) == 0:
#                 parol_2 = (pole_2[j+k])
#                 result.extend(pole_2[j], parol_2)
#             k += 1
#
#         print(pole_1[i], "-", result)
#         j += 1