def rotate(arr, k):
    """
    Rotate array A K times; that is, each element of A will be shifted
    to the right K times.
    """

    return arr[-(k % len(arr)):] + arr[:-(k % len(arr))]


def main():
    assert rotate([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert rotate([0, 0, 0], 1) == [0, 0, 0]
    assert rotate([1, 2, 3, 4], 4) == [1, 2, 3, 4]
    print('Hurray!')


if __name__ == '__main__':
    main()
