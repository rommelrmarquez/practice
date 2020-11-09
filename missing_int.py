def missing_int(A):
    """
    Given an array A of N integers, return the smallest positive
    integer (greater than 0) that does not occur in A.
    """

    return min(set(range(1, len(A) + 2)) - set(A))


def main():
    assert missing_int([1, 3, 6, 4, 1, 2]) == 5
    assert missing_int([1, 2, 3]) == 4
    assert missing_int([-1, -1, -1, -5]) == 1
    assert missing_int([1, 3, 6, 4, 1, 7, 8, 10]) == 2
    print('Hurray!')


if __name__ == '__main__':
    main()
