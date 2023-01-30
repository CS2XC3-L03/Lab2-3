import matplotlib.pyplot as plt
import sys
from good_sorts import *
from utils import time_sort
from bad_sorts import create_random_list

"""
Experiment 4: Compare the performance of the three good sorts.
"""

sys.setrecursionlimit(5200)


def main():
    NUM_OF_RUNS = 100
    xs = [10, 100, 1000, 2000]
    time_quick_sort, time_heap_sort, time_merge_sort = [], [], []
    for i in xs:
        L = create_random_list(i, i)
        time_quick_sort.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        time_heap_sort.append(time_sort(heapsort, L[:], NUM_OF_RUNS))
        time_merge_sort.append(time_sort(mergesort, L[:], NUM_OF_RUNS))

    # plot data
    plt.plot(xs, time_quick_sort, label="Quick Sort")
    plt.plot(xs, time_heap_sort, label="Heap Sort")
    plt.plot(xs, time_merge_sort, label="Merge Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    print("plotting")
    plt.show()


if __name__ == "__main__":
    main()
