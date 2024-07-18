import random


def create_random_list(length, max_value):
    """Create a random list of length "length" containing whole numbers between 0 and max_value inclusive."""
    return [random.randint(0, max_value) for _ in range(length)]


def create_near_sorted_list(length, max_value, swaps):
    """Create a near sorted list by creating a random list, sorting it, then doing a random number of swaps."""
    array = create_random_list(length, max_value)
    array.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(array, r1, r2)
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def insertion_sort(array):
    for i in range(1, len(array)):
        insert(array, i)


def insert(array, i):
    while i > 0:
        if array[i] < array[i - 1]:
            swap(array, i - 1, i)
            i -= 1
        else:
            return


# Improved insertion sort
def insertion_sort2(array):
    for i in range(1, len(array)):
        insert2(array, i)


def insert2(array, i):
    value = array[i]
    while i > 0:
        if array[i - 1] > value:
            array[i] = array[i - 1]
            i -= 1
        else:
            array[i] = value
            return
    array[0] = value


def bubble_sort(array):
    for _ in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j + 1)


# Improved Bubble sort
def bubble_sort2(array):
    for i in range(len(array) - 1):
        min_index = find_min_index(array, i)
        min_val = array[min_index]
        for j in range(min_index, i, -1):
            array[j] = array[j - 1]
        array[i] = min_val


def selection_sort(array):
    for i in range(len(array)):
        min_index = find_min_index(array, i)
        swap(array, i, min_index)


def find_min_index(array, n):
    min_index = n
    for i in range(n + 1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
    return min_index


# Improved Selection sort
def selection_sort2(array):
    for i in range(len(array) // 2):
        min_index, max_index = find_min_max_indices(array, i)
        swap(array, max_index, len(array) - 1 - i)
        swap(array, min_index, i)


def find_min_max_indices(array, n):
    min_index = max_index = n
    for i in range(n + 1, len(array) - n):
        if array[i] < array[min_index]:
            min_index = i
        if array[i] > array[max_index]:
            max_index = i
    return min_index, max_index
