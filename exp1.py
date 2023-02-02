import matplotlib.pyplot as plt
from bad_sorts import (
    create_random_list,
    insertion_sort,
    selection_sort,
    bubble_sort,
)
from utils import time_sort

"""
Experiment 1: Compare the performance of the three bad sorts.
"""


def main():
    NUM_OF_RUNS = 100
    xs = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000]
    time_insertion, time_selection, time_bubble = [], [], []
    for i in xs:
        L = create_random_list(i, i)
        print(f'start sorting (length={i})...')
        print('insertion sort...')
        time_insertion.append(time_sort(insertion_sort, L[:], NUM_OF_RUNS))
        print('selection sort...')
        time_selection.append(time_sort(selection_sort, L[:], NUM_OF_RUNS))
        print('bubble sort...')
        time_bubble.append(time_sort(bubble_sort, L[:], NUM_OF_RUNS))
        print('done')
    print('plotting...')
    # plot data
    plt.plot(xs, time_insertion, label="Insertion")
    plt.plot(xs, time_selection, label="Selection")
    plt.plot(xs, time_bubble, label="Bubble")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("Array length (n)")
    plt.ylabel("Time (s)")
    plt.title("Time to sort an Array of length n")
    plt.show()


if __name__ == "__main__":
    main()
