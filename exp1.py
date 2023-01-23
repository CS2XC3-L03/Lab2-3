import matplotlib.pyplot as plt
from bad_sorts import *
from utils import time_sort


def main():
    NUM_OF_RUNS = 10
    xs = [10, 50, 100, 500, 1000, 10000]
    time_insertion = []
    time_selection = []
    time_bubble = []
    for i in xs:
        L = create_random_list(i, 100)
        time_insertion.append(time_sort(insertion_sort, L, NUM_OF_RUNS))
        time_selection.append(time_sort(selection_sort, L, NUM_OF_RUNS))
        time_bubble.append(time_sort(bubble_sort, L, NUM_OF_RUNS))

    # Plot the results
    plt.plot(xs, time_insertion, label="Insertion")
    plt.plot(xs, time_selection, label="Selection")
    plt.plot(xs, time_bubble, label="Bubble")
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    plt.show()


if __name__ == "__main__":
    main()
