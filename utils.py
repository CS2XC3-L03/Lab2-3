import timeit as t


def time_sort(sort, L, num_of_runs):
    """
    Time the sort function on the list L for num_of_runs times.
    """
    sum = 0
    for _ in range(num_of_runs):
        start = t.default_timer()
        sort(L[:])
        end = t.default_timer()
        sum += end - start
    return sum / num_of_runs
