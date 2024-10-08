calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info():
    count_calls()
    string = str(input("Введите любую строку: "))
    new_string = (len(string), string.upper(), string.lower())
    print(new_string)
    # return new_string

def is_contains():
    count_calls()
    string = str(input("Введите строку для проверки наличия в списке: "))
    global list_to_search
    list_to_search = list(input("Напишите список: ").split())
    # print(list_to_search)
    if string in list_to_search:
        print("True")
        print("Строка", string, "входит в список", list_to_search)
    else:
        print("False")
        print("Строка", string, "не входит в список", list_to_search)

def cont():
    contin = str(input("Продолжим? (y/n) "))
    if contin == "y":
        string_info()
        is_contains()
        cont()
    else:
        print("Спасибо!")

string_info()
is_contains()
cont()
print(calls)
