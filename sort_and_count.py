"""
Sort array and count the number of inversiones in it.
"""


def sort_and_count(array):
    """ Recursively count the number of inversions in array
        and sort it using merge.
        Returns tuple (sorted array, number_of_inversions). """

    n = len(array)

    if n == 1 or n == 0:
        return array, 0
    else:
        a, x = sort_and_count(array[0:n/2])
        b, y = sort_and_count(array[n/2:n])
        c, z = merge_and_count_split(a, b)
        return c, z + x + y


def merge_and_count_split(a, b):
    """ Merge given arrays and count inversions in result one.
        Return tuple (sorted_array, number_of_inversions). """

    a_len = len(a)
    b_len = len(b)
    all_len = a_len + b_len

    i = 0  # iterator over 'a' array
    j = 0  # iterator over 'b' array
    res = []
    count = 0

    for k in range(0, all_len):
        if i >= a_len:
            res.extend(b[j:])
            break
        elif j >= b_len:
            res.extend(a[i:])
            break
        else:
            if a[i] <= b[j]:
                res.append(a[i])
                i += 1
            else:
                res.append(b[j])
                j += 1
                count += a_len - i

    return res, count

if __name__ == '__main__':
    print "Sort array and count the number of inversions in it. "
    print "Some tests:"
    test = []
    test.append([1, 9, 5, 2, 6, 7, 3])
    test.append([])
    test.append([2])
    test.append([1, 3, 2])
    test.append([5, 4, 3, 2, 1])
    test.append([5, 2, 3, 4, 6])
    test.append([5, 2, 3, 4, 1])
    test.append([1, 1, 1, 4, 5])

    for arr in test:
        print 'input:   ',
        for i in arr:
            print str(i) + ',',
        print '\noutput:', sort_and_count(arr)
        print

    while True:
        inp = raw_input("array>> ")
        if inp in ['q', 'quit', 'exit']:
            break

        array = []
        try:
            for i in inp.split(','):
                array.append(int(i))

            result = sort_and_count(array)
            print '  input:  ', array
            print '  output:', result
            print

        except ValueError:
            print "    expected list of integers or 'q'"
