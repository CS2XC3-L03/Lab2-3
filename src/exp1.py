import matplotlib.pyplot as plt
from bad_sorts import (
    create_random_list,
    insertion_sort,
    selection_sort,
    bubble_sort,
)
from utils import time_sort


def main():
    """
    Experiment 1: Compare the performance of the three bad sorts.
    """

    number_of_runs = 100
    intervals = [10, 50, 100, 500, 1000, 2000, 3000, 4000, 5000]
    time_insertion, time_selection, time_bubble = [], [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (length={interval})...")
        print("insertion sort...")
        time_insertion.append(time_sort(insertion_sort, array[:], number_of_runs))
        print("selection sort...")
        time_selection.append(time_sort(selection_sort, array[:], number_of_runs))
        print("bubble sort...")
        time_bubble.append(time_sort(bubble_sort, array[:], number_of_runs))
        print("done")

    print("plotting...")

    plt.plot(intervals, time_insertion, label="Insertion")
    plt.plot(intervals, time_selection, label="Selection")
    plt.plot(intervals, time_bubble, label="Bubble")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Performance of bad Sorts on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
