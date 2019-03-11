def fib(n):
    """ рекурсивное вычисление чисел фибоначчи """
    if n <= 1:
        return 1
    return (fib(n-1) + fib(n-2))

### __main__() ###

#print(str(fib(30)))

A = [0, 1] + [0] * 48

for i in range(2,50):
    A[i] = A[i-1] + A[i-2]
print(A[49])
