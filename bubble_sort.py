def bubble_sort(X):
    """ сортировка пузырьком """
    A = X[:]
    for i in range(0,len(A)-1):
        for j in range(0,len(A)-1-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A


def test_func(func,A,B):
    print "Input array: %r" % A
    C = func(A)
    print "Result array: %r" % C
    if C == B:
        return True
    else:
        return False

##### __main()__ #####

Array1 = [4, 2, 5, 1, 3, 0]
Right1 = [0, 1, 2, 3, 4, 5]

Array2 = [0, 10, 0, 10, 0]
Right2 = [0, 0, 0, 10, 10]

Array3 = [100, 1, 50]
Right3 = [1, 50, 100]


if test_func(bubble_sort, Array1, Right1):
    print "correct insert sort"
else:
    print "errored insert sort"

if test_func(bubble_sort, Array2, Right2):
    print "correct insert sort"
else:
    print "errored insert sort"

if test_func(bubble_sort, Array3, Right3):
    print "correct insert sort"
else:
    print "errored insert sort"
