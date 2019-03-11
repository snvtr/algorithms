def gcb(a, b):
    if b != 0:
        if a > b:
            return gcb(b, a % b)
        elif a < b:
            return gcb(a, b % a)
    return a
 
 
#a = int(input())
#b = int(input())
 
print(gcb(44, 8))

