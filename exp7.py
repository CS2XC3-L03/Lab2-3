import matplotlib.pyplot as plt
from sys import setrecursionlimit
from good_sorts import mergesort, bottom_up_mergesort
from bad_sorts import create_random_list
from utils import time_sort

"""
Compare the performance of mergesort and bottom-up mergesort
"""

setrecursionlimit(5200)


def main():
    NUM_OF_RUNS = 100
    xs = [10, 50, 100, 500, 1000, 5000]
    time_merge_sort, time_bottom_up_merge_sort = [], []

    for i in xs:
        L = create_random_list(i, i)
        print(f"start sorting (list size={i})...")
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, L[:], NUM_OF_RUNS))
        print("bottom-up merge sort...")
        time_bottom_up_merge_sort.append(
            time_sort(bottom_up_mergesort, L[:], NUM_OF_RUNS)
        )
        print("done")

    print("plotting...")
    # plot data
    plt.plot(xs, time_merge_sort, label="Merge Sort")
    plt.plot(xs, time_bottom_up_merge_sort, label="Bottom-up Merge Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("List size (n)")
    plt.ylabel("Time (s)")
    plt.title("Mergesort vs Bottom-up Mergesort on Lists of Size n")
    plt.show()


if __name__ == "__main__":
    main()
