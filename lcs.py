def lcs(A, B):
    """ поиск наибольшей общей последовательности """
    F = [ [0] * (len(B) + 1) for i in range(len(A) + 1)]

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i-1] == B[j-1]:
#                print('A[%d] == B[%d]' % (i-1,j-1))
                F[i][j] = 1 #+ F[i-1][j-1]
#            else:
#                F[i][j] = max(F[i-1][j], F[i][j-1])

    return F


A = [1, 5, 4, 3, 7, 9, 10, 12, 15]
B = [0, 2, 5, 4, 3, 8, 10, 12, 14]

C = lcs(A, B)
for i in range(len(C)):
    print(C[i])
i = 0
while i < len(C):
    j = 0
    while j < len(C[i]):
        while C[i][j] > 0:
            print('%d' % A[i-1])
            i += 1
            j += 1
        j += 1
    i += 1

