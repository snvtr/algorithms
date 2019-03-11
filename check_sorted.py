def check_sorted(A, ascending=True):
    """ Проверка отсортированности массива за O(n) """

    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0,len(A)-1):
        if s*A[i] > s*A[i+1]:
            flag = False
            break

    return flag

X = [1, 4, 3]

if check_sorted(X,True):
    print("True")
else:
    print("False")
            
