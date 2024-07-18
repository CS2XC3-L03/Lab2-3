import matplotlib.pyplot as plt
from good_sorts import quicksort, mergesort
from bad_sorts import create_random_list, insertion_sort
from utils import time_sort


def main():
    """
    Experiment 8: Determine size when insertion sort is more performant
    """

    number_of_runs = 10000
    intervals = [i + 1 for i in range(40)]
    time_insertion_sort, time_quick_sort, time_merge_sort = [], [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (list size={interval})...")
        print("insertion sort...")
        time_insertion_sort.append(time_sort(insertion_sort, array[:], number_of_runs))
        print("quick sort...")
        time_quick_sort.append(time_sort(quicksort, array[:], number_of_runs))
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, array[:], number_of_runs))
        print("done")

    print("plotting...")

    plt.plot(intervals, time_insertion_sort, label="Insertion sort")
    plt.plot(intervals, time_quick_sort, label="Quicksort")
    plt.plot(intervals, time_merge_sort, label="Merge sort")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Insertion sort vs quicksort vs merge sort on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
