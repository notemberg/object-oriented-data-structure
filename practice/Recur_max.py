def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_of_rest else max_of_rest

numbers = [5, 3, 8, 2, 9]
print(f"The maximum value in the list is {find_max(numbers)}")