import timeit as t


def time_sort(sort, L, num_of_runs):
    sum = 0
    for _ in range(num_of_runs):
        start = t.default_timer()
        sort(L)
        end = t.default_timer()
        sum += end - start
    return sum / num_of_runs
