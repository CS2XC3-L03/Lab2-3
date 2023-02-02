import matplotlib.pyplot as plt
import sys
from good_sorts import quicksort, quicksort2
from bad_sorts import create_random_list
from utils import time_sort

"""
Experiment 6: Compare the performance of the two quick sorts.
"""

sys.setrecursionlimit(5200)

def main():
    NUM_OF_RUNS = 100
    xs = [10, 100, 1000, 2000, 4000]
    time_quick_sort1, time_quick_sort2 = [], []
    for i in xs:
        L = create_random_list(i, i)
        time_quick_sort1.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        time_quick_sort2.append(time_sort(quicksort2, L[:], NUM_OF_RUNS))

    # plot data
    plt.plot(xs, time_quick_sort1, label="Quick Sort")
    plt.plot(xs, time_quick_sort2, label="Improved Quick Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("Array length (n)")
    plt.ylabel("Time (s)")
    plt.title("Quicksort vs Improved Quicksort on an Array of length n")
    print('plotting')
    plt.show()


if __name__ == "__main__":
    main()