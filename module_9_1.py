def apply_all_func(int_list, *functions):
    result = {}
    for functions in functions:
        res = functions(int_list)
        result[functions.__name__] = res
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))