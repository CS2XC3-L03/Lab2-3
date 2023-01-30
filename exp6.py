import matplotlib.pyplot as plt
import sys
from good_sorts import quicksort, quicksort2
from utils import time_sort
from bad_sorts import create_random_list

"""
Experiment 4: Compare the performance of the three good sorts.
"""

sys.setrecursionlimit(5200)

def main():
    NUM_OF_RUNS = 100
    xs = [10, 100, 1000, 2000, 4000]
    time_quick_sort1, time_quick_sort2 = [], []
    for i in xs:
        L = create_random_list(i, i)
        time_quick_sort1.append(time_sort(quicksort, L, NUM_OF_RUNS))
        time_quick_sort2.append(time_sort(quicksort2, L, NUM_OF_RUNS))

    # plot data
    plt.plot(xs, time_quick_sort1, label="Quick Sort")
    plt.plot(xs, time_quick_sort2, label="Improved Quick Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    print('plotting')
    plt.show()


if __name__ == "__main__":
    main()