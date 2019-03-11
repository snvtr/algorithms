def merge(A:list, B:list):

    C = [0]*(len(A) + len(B))

    a = b = c = 0
    while a < len(A) and b < len(B):
        if A[a] <= B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    while a < len(A):
        C[c] = A[a]
        a += 1
        c += 1
        
    while b < len(B):
        C[c] = B[b]
        b += 1
        c += 1

    return C

def merge_sort(S):

    if len(S) <= 1:
        return

    middle = len(S) // 2
    L = S[:middle]
    R = S[middle:]

    print("Before L: %r. R: %r" % (L, R))
    merge_sort(L)
    merge_sort(R)
    print("After L: %r. R: %r" % (L, R))
    C = merge(L, R)
    for i in range(len(S)):
        S[i] = C[i]

X = [5, 2, 1, 7, 0, 3, 2]

merge_sort(X)
print(X)
