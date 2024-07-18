from sys import setrecursionlimit
import matplotlib.pyplot as plt
from bad_sorts import create_near_sorted_list
from good_sorts import quicksort, mergesort, heapsort
from utils import time_sort


setrecursionlimit(5200)


def main():
    """
    Experiment 5: How much "unsorted" will let quick sort faster than merge sort and heap sort?
    """

    number_of_runs = 100
    intervals = [0, 10, 50, 100, 500, 1000, 5000]
    time_quick_sort, time_heap_sort, time_merge_sort = [], [], []

    for interval in intervals:
        array = create_near_sorted_list(2000, 2000, interval)
        print(f"start sorting (#swaps={interval})...")
        print("quick sort...")
        time_quick_sort.append(time_sort(quicksort, array[:], number_of_runs))
        print("heap sort...")
        time_heap_sort.append(time_sort(heapsort, array[:], number_of_runs))
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, array[:], number_of_runs))
        print("done")

    print("plotting...")

    plt.plot(intervals, time_quick_sort, label="Quicksort")
    plt.plot(intervals, time_heap_sort, label="Heap sort")
    plt.plot(intervals, time_merge_sort, label="Merge sort")

    plt.legend()
    plt.xlabel("Number of swaps (n)")
    plt.ylabel("Time (s)")
    plt.title(
        "Quicksort vs heap sort vs merge sort on near-sorted list of size 2000 with n swaps"
    )

    plt.show()


if __name__ == "__main__":
    main()
