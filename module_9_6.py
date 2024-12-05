# Сделала в двух вариантах. Закомментированный вариант выдаёт больше
# возможных сочетаний для строки любой длины

def  all_variants(text):
    # i = 0
    # while i != len(text):
    #     yield text[i]
    #     i += 1
    # for m in range(len(text)):
    #     i = 0
    #     if m == 0:
    #         m = 1
    #         continue
    #     while i != len(text) - m:
    #         yield text[i] + text[i+m]
    #         i += 1
    # for m in range(len(text) - 1):
    #     i = 0
    #     if m == 0:
    #         m = 1
    #         continue
    #     while i != len(text) - (m+1):
    #         yield text[i] + text[i+m] + text[i+m+1]
    #         i += 1
    m1 = [text[i] for i in range(len(text))]
    m2 = [text[i] + text[i+1] for i in range(len(text) - 1)]
    m3 = [text[i] + text[i+1] + text[i+2] for i in range(len(text) - 2)]
    return m1 + m2 + m3

a = all_variants("abc")
for i in a:
    print(i)