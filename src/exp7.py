import matplotlib.pyplot as plt
from sys import setrecursionlimit
from good_sorts import mergesort, bottom_up_mergesort
from bad_sorts import create_random_list
from utils import time_sort


setrecursionlimit(5200)


def main():
    """
    Experiment 7: Compare the performance of merge sort and bottom-up merge sort
    """

    number_of_runs = 100
    intervals = [10, 50, 100, 500, 1000, 5000]
    time_merge_sort, time_bottom_up_merge_sort = [], []

    for interval in intervals:
        array = create_random_list(interval, interval)
        print(f"start sorting (list size={interval})...")
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, array[:], number_of_runs))
        print("bottom-up merge sort...")
        time_bottom_up_merge_sort.append(
            time_sort(bottom_up_mergesort, array[:], number_of_runs)
        )
        print("done")

    print("plotting...")

    plt.plot(intervals, time_merge_sort, label="Merge sort")
    plt.plot(intervals, time_bottom_up_merge_sort, label="Bottom-up merge sort")

    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Merge sort vs bottom-up merge sort on lists of size n")

    plt.show()


if __name__ == "__main__":
    main()
