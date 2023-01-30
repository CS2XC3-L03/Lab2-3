import matplotlib.pyplot as plt
from bad_sorts import create_near_sorted_list, bubble_sort, selection_sort, insertion_sort
from utils import time_sort

"""
Experiment 1: Compare the performance of the three bad sorts.
"""


def main():
    NUM_OF_RUNS = 10
    swaps = [i for i in range(11)]
    time_insertion, time_selection, time_bubble = [], [], []
    for i in swaps:
        L = create_near_sorted_list(2000, 100, i)
        time_insertion.append(time_sort(insertion_sort, L, NUM_OF_RUNS))
        time_selection.append(time_sort(selection_sort, L, NUM_OF_RUNS))
        time_bubble.append(time_sort(bubble_sort, L, NUM_OF_RUNS))

    # plot data
    plt.plot(swaps, time_insertion, label="Insertion")
    plt.plot(swaps, time_selection, label="Selection")
    plt.plot(swaps, time_bubble, label="Bubble")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    plt.show()


if __name__ == "__main__":
    main()
