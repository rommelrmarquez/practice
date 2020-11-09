def bin_gap(n):
    """
    Return the maximal sequence of consecutive zeros that is surrounded
    by ones at both ends in the binary representation of N.
    """

    str_bin = str(bin(n))[2:]
    return max(list(map(len, str_bin.split('1')))[:-1])


def main():
    assert bin_gap(42) == 1
    assert bin_gap(9) == 2
    assert bin_gap(529) == 4
    assert bin_gap(32) == 0
    assert bin_gap(1041) == 5
    print('Hurray!')


if __name__ == '__main__':
    main()
