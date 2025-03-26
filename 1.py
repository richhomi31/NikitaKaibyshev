dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_4 = dict_1 | dict_2
dict_3 = {**dict_1, **dict_2}
dict_1.update(dict_2)

print(dict_4)
print(dict_3)
print(dict_1)