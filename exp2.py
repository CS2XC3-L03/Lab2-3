import matplotlib as mpl
import matplotlib.pyplot as plt
from utils import time_sort
from bad_sorts import selection_sort2, bubble_sort2, create_random_list

"""
Experiment 2: Compare the performance of the improved versions of selection sort and bubble sort.
"""


def main():
    NUM_OF_RUNS = 10
    xs = [10, 100, 1000, 10000]
    time_selection = []
    time_bubble = []
    for i in xs:
        L = create_random_list(i, 100)
        time_selection.append(time_sort(selection_sort2, L, NUM_OF_RUNS))
        time_bubble.append(time_sort(bubble_sort2, L, NUM_OF_RUNS))
    plt.plot(xs, time_selection, label="Selection")
    plt.plot(xs, time_bubble, label="Bubble")
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    plt.show()


if __name__ == "__main__":
    main()
