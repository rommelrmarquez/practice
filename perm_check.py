"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once,
and only once.

For example, array A such that:
    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation.
"""
from collections import defaultdict


def perm_check(A):
    """ Check if A is a valid permutation."""

    seen = defaultdict(int)
    for i in A:
        if seen.get(i) or i > len(A):
            return False
        seen[i] = 1
    return True


def perm_missing(A):
    """Return the missing element to complete the perm."""

    return list(set(range(1, len(A) + 2)) - set(A))[0]



def main():
    assert perm_check([3, 4, 1, 2, 5]) is True
    assert perm_check([3, 4, 1, 2, 5, 2]) is False
    assert perm_check([4, 1, 3]) is False

    assert perm_missing([3, 1, 2, 5]) == 4
    print('Hurray!')


if __name__ == '__main__':
    main()
