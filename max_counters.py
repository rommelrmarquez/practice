"""
    You are given N counters, initially set to 0, and you have two possible
    operations on them:

    increase(X) − counter X is increased by 1,
    max counter − all counters are set to the maximum value of any counter.
    A non-empty array A of M integers is given. This array represents
    consecutive operations:

    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    For example, given integer N = 5 and array A such that:

        A[0] = 3
        A[1] = 4
        A[2] = 4
        A[3] = 6
        A[4] = 1
        A[5] = 4
        A[6] = 4
    the values of the counters after each consecutive operation will be:
        (0, 0, 1, 0, 0)
        (0, 0, 1, 1, 0)
        (0, 0, 1, 2, 0)
        (2, 2, 2, 2, 2)
        (3, 2, 2, 2, 2)
        (3, 2, 2, 3, 2)
        (3, 2, 2, 4, 2)
    The goal is to calculate the value of every counter after all operations.
"""


def max_counter(N, A):
    """
    Return the final counts of the N counters.
    """

    counters = [0] * N
    max_count = 0
    prev_max = 0
    for num in A:
        if 1 <= num <= N:
            counters[num - 1] += 1
            if counters[num - 1] > max_count:
                prev_max = max_count
                max_count = counters[num - 1]
        elif num == N + 1 and prev_max != max_count:
            counters = [max_count] * N
    return counters


def main():
    assert max_counter(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
    assert max_counter(5, [6, 6, 6, 6, 6, 6, 6]) == [0, 0, 0, 0, 0]
    print('Hurray!')


if __name__ == '__main__':
    main()
