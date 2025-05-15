def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_of_rest = find_min(lst[1:])
        return lst[0] if lst[0] < min_of_rest else min_of_rest

numbers = [5, 3, 8, 2, 9]
print(f"The minimum value in the list is {find_min(numbers)}")