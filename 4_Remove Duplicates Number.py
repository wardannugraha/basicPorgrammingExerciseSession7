list_number = [1, 2, 3, 4, 2, 3, 5, 6, 1]
list_number_no_duplicate = []
for item in list_number :
    if item not in list_number_no_duplicate :
        list_number_no_duplicate.append(item)
print(list_number_no_duplicate)