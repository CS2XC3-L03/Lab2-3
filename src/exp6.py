import matplotlib.pyplot as plt
from sys import setrecursionlimit
from good_sorts import quicksort, quicksort2
from bad_sorts import create_random_list
from utils import time_sort


setrecursionlimit(100200)


def main():
    """
    Experiment 6: Compare the performance of quicksort and dual pivot quicksort.
    """

    number_of_runs = 100
    intervals = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    time_quick_sort1, time_quick_sort2 = [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (length={interval})...")
        print("quicksort...")
        time_quick_sort1.append(time_sort(quicksort, array[:], number_of_runs))
        print("dual pivot quicksort...")
        time_quick_sort2.append(time_sort(quicksort2, array[:], number_of_runs))
        print("done")

    print("plotting...")

    plt.plot(intervals, time_quick_sort1, label="Quicksort")
    plt.plot(intervals, time_quick_sort2, label="Dual-pivot quicksort")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Quicksort vs dual-pivot quicksort on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
