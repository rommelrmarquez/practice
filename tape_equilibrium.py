"""
    A non-empty array A consisting of N integers is given. Array A
    represents numbers on a tape.

    Any integer P, such that 0 < P < N, splits this tape into two non-empty
    parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

    The difference between the two parts is the value of: |(A[0] + A[1] + ... +
    A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
"""


def tape_eq(A):
    """Returns the minimal difference that can be achieved."""

    total = sum(A)
    min_diff = abs(max(A) - min(A))
    curr_sum = 0
    for i in A[:-1]:
        curr_sum += i
        curr_diff = abs(total - 2 * curr_sum)
        if curr_diff < min_diff:
            min_diff = curr_diff
    return min_diff


def main():
    assert tape_eq([-1, 0, -1, 1, 1, -1, 0, 1, -1]) == 1
    assert tape_eq([-1, 1]) == 2
    print('Hurray!')


if __name__ == '__main__':
    main()
