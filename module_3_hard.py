def calculate_structure_sum(data_structure):
    result = 0
    for item in ds:
        if isinstance(item, int):
            result += int(item)
        elif isinstance(item, str):
            result += len(item)
        else:
            for key, value in lst4.items():
                result += (len(key) + int(value))
            for item in lst3:
                if isinstance(item, int):
                    result += int(item)
                    print(f"3- {result}")
                elif isinstance(item, str):
                    result += len(item)
                    print(f"3- {result}")
                else:
                    calculate_structure_sum(data_structure) == len(lst1[0]) + lst1[1]
                    # for item in lst1:
                    #     if isinstance(item, int):
                    #         result = int(item) + calculate_structure_sum(item)
                    #         print(f"1_1- {result}")
                    #         return result
                    #     else:
                    #         isinstance(item, str)
                    #         result = len(item) #+ calculate_structure_sum(int(i) - 1)
                    #         print(f"1_2- {result}")
                    #     return result
                    break
                return result + calculate_structure_sum(data_structure)
        # return result
    return result

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
lst1 = ('Urban2', 35)
lst2 = (2, 'Urban', lst1)
lst3 = ((), [{lst2}])
lst4 = {'cube': 7, 'drum': 8}
lst5 = (6, lst4, "Hello", lst3)
lst6 = {'a': 4, 'b': 5}
lst7 = [1, 2, 3]
ds = [lst7, lst6, lst5, "Hello", lst3]
first = len(lst1[0])
calculate_structure_sum(data_structure)
print(calculate_structure_sum(data_structure))