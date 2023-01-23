import matplotlib as mpl
import matplotlib.pyplot as plt
from utils import time_sort
from bad_sorts import selection_sort2, bubble_sort2, create_random_list


def test_sorts(L):
    NUM_OF_RUNS = 10
    return (
        time_sort(selection_sort2, L, NUM_OF_RUNS),
        time_sort(bubble_sort2, L, NUM_OF_RUNS),
    )


def main():
    xs = [10, 100, 1000, 10000]
    time_selection = []
    time_bubble = []
    for i in xs:
        L = create_random_list(i, 100)
        v1, v2 = test_sorts(L)
        time_selection.append(v1)
        time_bubble.append(v2)
    plt.plot(xs, time_selection, label="Selection")
    plt.plot(xs, time_bubble, label="Bubble")
    plt.legend()
    plt.xlabel("List length")
    plt.ylabel("Time (s)")
    plt.title("Time to sort a list of length n")
    plt.show()


if __name__ == "__main__":
    main()
