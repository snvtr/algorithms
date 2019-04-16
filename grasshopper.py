def trajectory(N:int):
    """ Fibonacchi sum: practical application, the grasshopper route """    
    K = [0,1] + [0]*N

    for i in range(2, N+1):
        K[i] = K[i-2] + K[i-1]

    return K[N-1]

def trajectory2(N:int, Allowed:list):
    """ Fibonacchi sum: practical application, the grasshopper route with banned points """    
    
    K = [0,1] + [0]*N

    for i in range(2, N+1):
        if Allowed[i]:
            K[i] = K[i-2] + K[i-1]
        else:
            K[i] = 0

    return K[N]


### __main__() ###

hops = 30

Allowed = [True for i in range(hops+1)]
Allowed[7] = False

print(str(trajectory2(hops,Allowed)))
