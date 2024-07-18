import math


def quicksort(array):
    copy = quicksort_copy(array)
    for i in range(len(array)):
        array[i] = copy[i]


def quicksort_copy(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left, right = [], []
    for num in array[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


# Improved quicksort
def quicksort2(array):
    copy = quicksort_copy2(array)
    for i in range(len(array)):
        array[i] = copy[i]


def quicksort_copy2(array):
    if len(array) < 2:
        return array
    lp, rp = min(array[0], array[1]), max(array[0], array[1])
    left, mid, right = [], [], []
    for num in array[2:]:
        if num < lp:
            left.append(num)
        elif lp <= num <= rp:
            mid.append(num)
        else:
            right.append(num)
    return (
        quicksort_copy2(left)
        + [lp]
        + quicksort_copy2(mid)
        + [rp]
        + quicksort_copy2(right)
    )


def mergesort(array):
    if len(array) <= 1:
        return
    mid = len(array) // 2
    left, right = array[:mid], array[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        array[i] = temp[i]


def merge(left, right):
    array = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            array.append(right[j])
            j += 1
        elif j >= len(right):
            array.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                array.append(left[i])
                i += 1
            else:
                array.append(right[j])
                j += 1
    return array


def bottom_up_mergesort(array):
    width, num = 1, len(array)
    while width < num:
        for i in range(0, num, 2 * width):
            array[i : i + 2 * width] = merge(
                array[i : i + width], array[i + width : i + 2 * width]
            )
        width *= 2


def heapsort(array):
    heap = Heap(array)
    for _ in range(len(array)):
        heap.extract_max()


class Heap:
    length = 0
    data = []

    def __init__(self, array):
        self.data = array
        self.length = len(array)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if (
            self.right(i) < self.length
            and self.data[self.right(i)] > self.data[largest_known]
        ):
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = (
                self.data[largest_known],
                self.data[i],
            )
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, array):
        for num in array:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = (
                self.data[self.parent(i)],
                self.data[i],
            )
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = (
            self.data[self.length - 1],
            self.data[0],
        )
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2**height
        s = ""
        for i in range(height):
            for j in range(2**i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s
