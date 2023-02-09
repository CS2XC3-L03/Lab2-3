import matplotlib.pyplot as plt
from sys import setrecursionlimit
from good_sorts import quicksort, quicksort2
from bad_sorts import create_random_list
from utils import time_sort

"""
Experiment 6: Compare the performance of quicksort and dual pivot quicksort.
"""

setrecursionlimit(100200)


def main():
    NUM_OF_RUNS = 100
    xs = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    time_quick_sort1, time_quick_sort2 = [], []
    for i in xs:
        L = create_random_list(i, i)
        print(f"start sorting (length={i})...")
        print("quicksort...")
        time_quick_sort1.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        print("dual pivot quicksort...")
        time_quick_sort2.append(time_sort(quicksort2, L[:], NUM_OF_RUNS))
        print("done")

    print("plotting...")
    # plot data
    plt.plot(xs, time_quick_sort1, label="Quick Sort")
    plt.plot(xs, time_quick_sort2, label="Dual Pivot Quick Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length (n)")
    plt.ylabel("Time (s)")
    plt.title("Quicksort vs Dual Pivot Quicksort on Lists of Size n")
    plt.show()


if __name__ == "__main__":
    main()
