def prefix(A):
    """ calculates the string prefix """

    Pi = [0] * (len(A))

    for i in range(1,len(A)):

        p = Pi[i-1]

        while p > 0 and A[p] != A[i]:
            p = Pi[p-1]

        if A[p] == A[i]:
            p += 1

        Pi[i] = p

    return Pi

S = 'in@string' # string search based on string prefix
                 

print(prefix(S))
