my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
set_list = []
for num in my_list:
    if num not in set_list:
        set_list.append(num)
    print(set_list)
