def set_gen(numbers):
    count_dict = {}
    result_set = set()

    for number in numbers:
        if number not in count_dict:
            count_dict[number] = 1
            result_set.add(number)
        else:
            count_dict[number] += 1
            result_set.add(str(number) * count_dict[number])

    return result_set

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3))
