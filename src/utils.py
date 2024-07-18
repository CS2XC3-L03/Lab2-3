import timeit


def time_sort(sort, array, num_of_runs):
    """
    Time the sort function on the array for num_of_runs times and return the average time.
    """
    total = 0
    for _ in range(num_of_runs):
        start = timeit.default_timer()
        sort(array[:])
        total += timeit.default_timer() - start
    return total / num_of_runs
