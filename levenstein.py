def levenstein(A, B):
    """ редакционное растояние между двумя строками """    

    # так получить массив понятнее чем вариантом ниже
    F = [[0]*(len(B)+1) for x in range(len(A)+1)]
    for j in range(len(A)+1):
        F[j][0] = j
    for j in range(1,len(B)+1):
        F[0][j] = j

    # более сложная декларация    
    #F = [[ i+j if i*j == 0 else 0 for j in range(len(B)+1) ]
    #      for i in range(len(A)+1) ]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j], F[i][j-1], F[i-1][j-1])

    for i in range(len(A)+1):
        print(F[i])
    return F[len(A)][len(B)]

### __main__() ###

A = 'malaka'
B = 'moloko'

print(levenstein(A, B))
