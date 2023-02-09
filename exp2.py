import matplotlib.pyplot as plt
from utils import time_sort
from bad_sorts import (
    selection_sort,
    selection_sort2,
    bubble_sort,
    bubble_sort2,
    create_random_list,
)

"""
Experiment 2: Compare the performance of the improved versions of selection sort and bubble sort.
"""


def main():
    NUM_OF_RUNS = 100
    xs = [10, 50, 100, 500, 1000, 5000]
    time_selection1, time_selection2 = [], []
    time_bubble1, time_bubble2 = [], []

    for i in xs:
        L = create_random_list(i, i)
        print(f"start sorting (length={i})...")
        print("bad selection sort...")
        time_selection1.append(time_sort(selection_sort, L[:], NUM_OF_RUNS))
        print("improved selection sort...")
        time_selection2.append(time_sort(selection_sort2, L[:], NUM_OF_RUNS))
        print("bad bubble sort...")
        time_bubble1.append(time_sort(bubble_sort, L[:], NUM_OF_RUNS))
        print("improved bubble sort...")
        time_bubble2.append(time_sort(bubble_sort2, L[:], NUM_OF_RUNS))
        print("done")

    print("plotting...")
    # plot data for selection sort
    plt.plot(xs, time_selection1, label="Bad Selection Sort")
    plt.plot(xs, time_selection2, label="Improved Selection Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length (n)")
    plt.ylabel("Time (s)")
    plt.title("Bad vs. Improved Selection Sort on Lists of Size n")
    plt.show()

    # plot data for bubble sort
    plt.plot(xs, time_bubble1, label="Bad Bubble Sort")
    plt.plot(xs, time_bubble2, label="Improved Bubble Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List length (n)")
    plt.ylabel("Time (s)")
    plt.title("Bad vs. Improved Bubble Sort on Lists of Size n")
    plt.show()


if __name__ == "__main__":
    main()
