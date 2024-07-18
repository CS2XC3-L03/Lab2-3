import matplotlib.pyplot as plt
from sys import setrecursionlimit
from bad_sorts import create_random_list
from good_sorts import quicksort, heapsort, mergesort
from utils import time_sort


setrecursionlimit(5200)


def main():
    """
    Experiment 4: Compare the performance of the three good sorts.
    """

    number_of_runs = 100
    intervals = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000]
    time_quick_sort, time_heap_sort, time_merge_sort = [], [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (length={interval})...")
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
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Performance of good sorts on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
