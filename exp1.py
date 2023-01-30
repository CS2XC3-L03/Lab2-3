import matplotlib.pyplot as plt
from bad_sorts import *
from utils import time_sort

"""
Experiment 1: Compare the performance of the three bad sorts.
"""


def main():
    NUM_OF_RUNS = 100
    xs = [10, 100, 1000, 5000]
    time_insertion, time_selection, time_bubble = [], [], []
    for i in xs:
        L = create_random_list(i, i)
        time_insertion.append(time_sort(insertion_sort, L[:], NUM_OF_RUNS))
        time_selection.append(time_sort(selection_sort, L[:], NUM_OF_RUNS))
        time_bubble.append(time_sort(bubble_sort, L[:], NUM_OF_RUNS))

    # plot data
    plt.plot(xs, time_insertion, label="Insertion")
    plt.plot(xs, time_selection, label="Selection")
    plt.plot(xs, time_bubble, label="Bubble")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    plt.show()


if __name__ == "__main__":
    main()
