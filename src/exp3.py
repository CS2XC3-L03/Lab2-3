import matplotlib.pyplot as plt
from bad_sorts import (
    create_near_sorted_list,
    insertion_sort2,
    selection_sort2,
    bubble_sort2,
)
from utils import time_sort


def main():
    """
    Experiment 3: Compare the performance of the three improved sorts, with increasing amounts of swaps.
    """

    number_of_runs = 100
    intervals = [0, 10, 50, 100, 500, 1000, 5000]
    time_insertion, time_selection, time_bubble = [], [], []

    for interval in intervals:
        array = create_near_sorted_list(5000, 5000, interval)
        print(f"start sorting (swaps={interval})...")
        print("insertion sort...")
        time_insertion.append(time_sort(insertion_sort2, array[:], number_of_runs))
        print("selection sort...")
        time_selection.append(time_sort(selection_sort2, array[:], number_of_runs))
        print("bubble sort...")
        time_bubble.append(time_sort(bubble_sort2, array[:], number_of_runs))
        print("done")

    print("plotting...")

    plt.plot(intervals, time_insertion, label="Insertion")
    plt.plot(intervals, time_selection, label="Selection")
    plt.plot(intervals, time_bubble, label="Bubble")

    plt.legend()
    plt.xlabel("Number of swaps (n)")
    plt.ylabel("Time (s)")
    plt.title(
        "Improved insertion, selection, and bubble sort on near-sorted list of size 5000 with n Swaps"
    )

    plt.show()


if __name__ == "__main__":
    main()
