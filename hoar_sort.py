def hoar_sort(A):
    """ поиск Хоара """

    L = []
    R = []
    M = []

    if len(A) <= 1:
        return

    barrier = A[0]
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)

    hoar_sort(L)
    hoar_sort(R)

    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

X = [4, 3, 5, 7, 6, 0, 2]

hoar_sort(X)
print(X)
