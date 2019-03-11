#!C:/Python36/python3.exe

def left_bound(A:list, key):
    left = -1
    right = len(A)

    while right - left > 1:

        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left

def right_bound(A:list, key):
    left = -1
    right = len(A)

    while right - left > 1:

        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right


### __main()___ ###

A = [1,3,3,5,6,7,9]

Left  = left_bound(A, 2)
Right = right_bound(A, 2)

print(A[Left], A[Right])
