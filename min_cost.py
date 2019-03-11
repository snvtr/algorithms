def min_cost(N:int, price:list):
    C = [float('-inf'), price[1], price[1] + price[2]] + \
         [0] * (N-2)

    for i in range(3, N+1):
         C[i] = price[i] + min(C[i-1],C[i-2])

    return C[N]


### __main__() ###

n = 10
prices = [1,2,4,3,6,5,3,2,4,3,2]

print(str(min_cost(n,prices)))
