dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

def max_dict(*dicts):
    max_dict = {}
    for dic in dicts:
        for key, value in dic.items():
            if key not in max_dict:
                max_dict[key] = value
            else:
                max_dict[key] = max(max_dict[key], value)
    return max_dict

def sum_dict(*dicts):
    sum_dict = {}
    for dic in dicts:
        for key, value in dic.items():
            if key not in sum_dict:
                sum_dict[key] = value
            else:
                sum_dict[key] += value
    return sum_dict

print(max_dict(dict_1, dict_2))
print(sum_dict(dict_1, dict_4, dict_3))
print(max_dict(dict_1, dict_2, dict_3, dict_4))
print(sum_dict(dict_1, dict_2, dict_3, dict_4))
