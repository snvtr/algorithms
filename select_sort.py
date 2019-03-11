def select_sort(X):
    A = X[:]
    for i in range(0,len(A)-1):
        for j in range(i+1,len(A)):
            if A[j] < A[i]:
                A[i], A[j] = A[j], A[i]

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

Array2 = [0, 0, 0, 0, 0]
Right2 = [0, 0, 0, 0, 0]

Array3 = [100, 1, 50]
Right3 = [1, 50, 100]


print "Ok" if test_func(select_sort, Array1, Right1) else "Fail"
print "Ok" if test_func(select_sort, Array2, Right2) else "Fail"
print "Ok" if test_func(select_sort, Array3, Right3) else "Fail"
