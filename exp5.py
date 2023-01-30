import sys
from good_sorts import quicksort, mergesort, heapsort
from bad_sorts import create_near_sorted_list
import matplotlib.pyplot as plt
from utils import time_sort

sys.setrecursionlimit(10200)

"""
Experiment 5: how much "unsorted" will let quick sort faster than merge sort and heap sort?
"""


def main():
    NUM_OF_RUNS = 100
    xs = [i * 1000 for i in range(0, 5)]
    time_quick_sort, time_heap_sort, time_merge_sort = [], [], []
    for i in xs:
        L = create_near_sorted_list(3000, 3000, i)
        print(f"start sorting (#swaps={i})...")
        print("quick sort...")
        time_quick_sort.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        print("heap sort...")
        time_heap_sort.append(time_sort(heapsort, L[:], NUM_OF_RUNS))
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, L[:], NUM_OF_RUNS))
        print("done")

    # plot data
    plt.plot(xs, time_quick_sort, label="Quick Sort")
    plt.plot(xs, time_heap_sort, label="Heap Sort")
    plt.plot(xs, time_merge_sort, label="Merge Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("# of swaps")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a near sorted list")
    plt.show()


if __name__ == "__main__":
    main()
