def gis(A):
    """ the longest increasing sequence
        and the index of its first element
    """
    M = 0
    m = 0
    idx = 0
    IDX = 0
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            m += 1
            if m == 2:
                idx = i-1
        else:
            if m > M:
                M = m
                IDX = idx
            m = 1
            
            
    return (M, IDX)

X = [1, 2, 3, 1, 2, 0, 1, 2, 3, 4, 1, 2]

(size, first) = gis(X)
print('Size: %d, First element: %d' % (size, first))
