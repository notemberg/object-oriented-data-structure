def bubble_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1] and not reverse) or (arr[j] < arr[j + 1] and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if (arr[j] < arr[idx] and not reverse) or (arr[j] > arr[idx] and reverse):
                idx = j
        arr[i], arr[idx] = arr[idx], arr[i]
    return arr

def insertion_sort(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and ((arr[j] > key and not reverse) or (arr[j] < key and reverse)):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def shell_sort(arr, reverse=False):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and ((arr[j - gap] > temp and not reverse) or (arr[j - gap] < temp and reverse)):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def heapify(arr, n, i, reverse):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and ((arr[left] > arr[largest] and not reverse) or (arr[left] < arr[largest] and reverse)):
        largest = left
    if right < n and ((arr[right] > arr[largest] and not reverse) or (arr[right] < arr[largest] and reverse)):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, reverse)

def heap_sort(arr, reverse=False):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, reverse)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, reverse)
    return arr

def merge_sort(arr, reverse=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half, reverse)
        merge_sort(right_half, reverse)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if (left_half[i] < right_half[j] and not reverse) or (left_half[i] > right_half[j] and reverse):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def partition(arr, low, high, reverse):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if (arr[j] <= pivot and not reverse) or (arr[j] >= pivot and reverse):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None, reverse=False):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high, reverse)
        quick_sort(arr, low, pi - 1, reverse)
        quick_sort(arr, pi + 1, high, reverse)
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

#Bubble Sort
# Ascending Order
sorted_arr = bubble_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = bubble_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Selection Sort
# Ascending Order
sorted_arr = selection_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = selection_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Insertion Sort
# Ascending Order
sorted_arr = insertion_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = insertion_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Shell Sort
# Ascending Order
sorted_arr = shell_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = shell_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Heap Sort
# Ascending Order
sorted_arr = heap_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = heap_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Merge Sort
# Ascending Order
sorted_arr = merge_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = merge_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]

#Quick Sort
# Ascending Order
sorted_arr = quick_sort(arr[:])  # [11, 12, 22, 25, 34, 64, 90]
# Descending Order
sorted_arr_desc = quick_sort(arr[:], reverse=True)  # [90, 64, 34, 25, 22, 12, 11]