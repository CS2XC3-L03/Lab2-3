import matplotlib.pyplot as plt
from good_sorts import quicksort, mergesort
from bad_sorts import create_random_list, insertion_sort
from utils import time_sort

"""
Upto what size is insertion sort is more performant
"""


def main():
    NUM_OF_RUNS = 10000
    xs = [i + 1 for i in range(40)]
    time_insertion_sort, time_quick_sort, time_merge_sort = [], [], []
    for i in xs:
        L = create_random_list(i, i)
        print(f"start sorting (list size={i})...")
        print("insertion sort...")
        time_insertion_sort.append(time_sort(insertion_sort, L[:], NUM_OF_RUNS))
        print("quick sort...")
        time_quick_sort.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, L[:], NUM_OF_RUNS))
        print("done")

    print("plotting...")
    # plot data
    plt.plot(xs, time_insertion_sort, label="Insertion Sort")
    plt.plot(xs, time_quick_sort, label="Quick Sort")
    plt.plot(xs, time_merge_sort, label="Merge Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Performance of Insertion sort, Quicksort and Mergesort on lists of size n")
    plt.show()


if __name__ == "__main__":
    main()
