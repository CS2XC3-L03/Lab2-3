import matplotlib.pyplot as plt
from bad_sorts import (
    create_near_sorted_list,
    insertion_sort2,
    selection_sort2,
    bubble_sort2,
)
from utils import time_sort

"""
Experiment 3: Compare the performance of the three improved sorts, with increasing amounts of swaps.
"""


def main():
    NUM_OF_RUNS = 100
    swaps = [0, 10, 50, 100, 500, 1000, 5000]
    time_insertion, time_selection, time_bubble = [], [], []
    for i in swaps:
        L = create_near_sorted_list(5000, 5000, i)
        print(f"start sorting (swaps={i})...")
        print("insertion sort...")
        time_insertion.append(time_sort(insertion_sort2, L[:], NUM_OF_RUNS))
        print("selection sort...")
        time_selection.append(time_sort(selection_sort2, L[:], NUM_OF_RUNS))
        print("bubble sort...")
        time_bubble.append(time_sort(bubble_sort2, L[:], NUM_OF_RUNS))
        print("done")

    print("plotting...")
    # plot data
    plt.plot(swaps, time_insertion, label="Insertion")
    plt.plot(swaps, time_selection, label="Selection")
    plt.plot(swaps, time_bubble, label="Bubble")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("Number of swaps (n)")
    plt.ylabel("Time (s)")
    plt.title(
        "Improved Insertion, Selection, and Bubble sort on Near-sorted Lists of Size 5000 With n Swaps"
    )
    plt.show()


if __name__ == "__main__":
    main()
