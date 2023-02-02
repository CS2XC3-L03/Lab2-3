import matplotlib.pyplot as plt
import sys
from bad_sorts import create_near_sorted_list
from good_sorts import quicksort, mergesort, heapsort
from utils import time_sort

"""
Experiment 5: how much "unsorted" will let quick sort faster than merge sort and heap sort?
"""

sys.setrecursionlimit(5200)

def main():
    NUM_OF_RUNS = 100
    xs = [0, 10, 50, 100, 500, 1000, 2000]
    time_quick_sort, time_heap_sort, time_merge_sort = [], [], []
    for i in xs:
        L = create_near_sorted_list(2000, 2000, i)
        print(f"start sorting (#swaps={i})...")
        print("quick sort...")
        time_quick_sort.append(time_sort(quicksort, L[:], NUM_OF_RUNS))
        print("heap sort...")
        time_heap_sort.append(time_sort(heapsort, L[:], NUM_OF_RUNS))
        print("merge sort...")
        time_merge_sort.append(time_sort(mergesort, L[:], NUM_OF_RUNS))
        print("done")

    print('plotting...')
    # plot data
    plt.plot(xs, time_quick_sort, label="Quick Sort")
    plt.plot(xs, time_heap_sort, label="Heap Sort")
    plt.plot(xs, time_merge_sort, label="Merge Sort")
    # add legend, label the axis, and give the plot a title
    plt.legend()
    plt.xlabel("Number of swaps (n)")
    plt.ylabel("Time (s)")
    plt.title("Quicksort vs Heapsort vs Mergesort on a near sorted array with n swaps")
    plt.show()


if __name__ == "__main__":
    main()
