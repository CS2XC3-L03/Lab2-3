import matplotlib.pyplot as plt
from bad_sorts import (
    create_near_sorted_list,
    bubble_sort,
    selection_sort,
    insertion_sort,
)
from utils import time_sort

"""
Experiment 3: Compare the performance of the three bad sorts, with increasing amounts of swaps.
"""


def main():
    NUM_OF_RUNS = 100
    swaps = [0, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]
    time_insertion, time_selection, time_bubble = [], [], []
    for i in swaps:
        L = create_near_sorted_list(5000, 5000, i)
        print(f'start sorting (swaps={i})...')
        print('insertion sort...')
        time_insertion.append(time_sort(insertion_sort, L[:], NUM_OF_RUNS))
        print('selection sort...')
        time_selection.append(time_sort(selection_sort, L[:], NUM_OF_RUNS))
        print('bubble sort...')
        time_bubble.append(time_sort(bubble_sort, L[:], NUM_OF_RUNS))
        print('done')

    # plot data
    plt.plot(swaps, time_insertion, label="Insertion")
    plt.plot(swaps, time_selection, label="Selection")
    plt.plot(swaps, time_bubble, label="Bubble")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("Number of swaps")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length 5000 with varying swaps")
    plt.show()


if __name__ == "__main__":
    main()
