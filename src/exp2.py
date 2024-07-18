import matplotlib.pyplot as plt
from utils import time_sort
from bad_sorts import (
    selection_sort,
    selection_sort2,
    bubble_sort,
    bubble_sort2,
    create_random_list,
)


def main():
    """
    Experiment 2: Compare the performance of the improved versions of selection sort and bubble sort.
    """

    number_of_runs = 100
    intervals = [10, 50, 100, 500, 1000, 5000]
    time_selection1, time_selection2 = [], []
    time_bubble1, time_bubble2 = [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (length={interval})...")
        print("bad selection sort...")
        time_selection1.append(time_sort(selection_sort, array[:], number_of_runs))
        print("improved selection sort...")
        time_selection2.append(time_sort(selection_sort2, array[:], number_of_runs))
        print("bad bubble sort...")
        time_bubble1.append(time_sort(bubble_sort, array[:], number_of_runs))
        print("improved bubble sort...")
        time_bubble2.append(time_sort(bubble_sort2, array[:], number_of_runs))
        print("done")

    print("plotting selection sort...")

    plt.plot(intervals, time_selection1, label="Bad selection sort")
    plt.plot(intervals, time_selection2, label="Improved selection sort")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Bad vs. improved selection sort on lists of size n")

    plt.show()

    print("plotting bubble sort...")

    plt.plot(intervals, time_bubble1, label="Bad bubble sort")
    plt.plot(intervals, time_bubble2, label="Improved bubble sort")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Bad vs. improved bubble sort on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
