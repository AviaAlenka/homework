from math import inf
def divide(first, second):
    if second == 0:
        print(inf)
        return inf
    else:
        print(int(first) / int(second))
